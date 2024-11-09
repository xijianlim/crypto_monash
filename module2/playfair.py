# %%
import plotly.graph_objects as go

def create_playfair_grid(keyword):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = "".join(dict.fromkeys(keyword.upper().replace("J", "I")))
    grid_letters = keyword + "".join([ch for ch in alphabet if ch not in keyword])
    grid = [list(grid_letters[i:i+5]) for i in range(0, 25, 5)]
    return grid

def find_position(grid, char):
    for row in range(5):
        for col in range(5):
            if grid[row][col] == char:
                return row, col
    return None

def prepare_text(plaintext):
    plaintext = plaintext.upper().replace("J", "I")
    pairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = plaintext[i + 1] if i + 1 < len(plaintext) else 'Z'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    if len(plaintext) % 2 != 0:
        pairs[-1] = pairs[-1][0] + 'Z' if len(pairs[-1]) == 1 else pairs[-1]
    return pairs

def encrypt_pair(grid, a, b):
    row_a, col_a = find_position(grid, a)
    row_b, col_b = find_position(grid, b)
    
    if row_a == row_b:
        encrypted_a = grid[row_a][(col_a + 1) % 5]
        encrypted_b = grid[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        encrypted_a = grid[(row_a + 1) % 5][col_a]
        encrypted_b = grid[(row_b + 1) % 5][col_b]
    else:
        encrypted_a = grid[row_a][col_b]
        encrypted_b = grid[row_b][col_a]
    
    return encrypted_a, encrypted_b, (row_a, col_a), (row_b, col_b)

def plot_grid(grid, pair_pos, title):
    z_data = [[0]*5 for _ in range(5)]  # Create a zero matrix for heatmap

    # Highlight the positions of the pair in the grid
    for pos in pair_pos:
        z_data[pos[0]][pos[1]] = 1  # Highlight cells with '1'

    # Create a heatmap with the Playfair grid
    fig = go.Figure(data=go.Heatmap(
        z=z_data,
        x=[str(i + 1) for i in range(5)],
        y=[str(5 - i) for i in range(5)],  # Adjust y-axis to display from top to bottom
        colorscale=["white", "lightblue"],  # Highlight color
        showscale=False,
        reversescale=True  # Flip the y-axis display order
    ))

    # Add grid letters as annotations
    for row in range(5):
        for col in range(5):
            fig.add_annotation(
                x=col, y=4 - row,  # Adjust y to match top-left to bottom-right
                text=grid[row][col],
                showarrow=False,
                font=dict(color="black" if z_data[row][col] == 0 else "blue", size=14)
            )

    fig.update_layout(
        title=title,
        xaxis=dict(showgrid=False, zeroline=False, tickvals=[]),
        yaxis=dict(showgrid=False, zeroline=False, tickvals=[]),
        height=400,
        width=400
    )

    fig.show()

def playfair_encrypt_visualize(plaintext, keyword):
    grid = create_playfair_grid(keyword)
    pairs = prepare_text(plaintext)
    encrypted_text = ""

    for i, (a, b) in enumerate(pairs):
        enc_a, enc_b, pos_a, pos_b = encrypt_pair(grid, a, b)
        encrypted_text += enc_a + enc_b

        # Plot each step of encryption
        title = f"Step {i + 1}: Encrypting '{a}{b}' to '{enc_a}{enc_b}'"
        plot_grid(grid, [pos_a, pos_b], title)

    return encrypted_text

# Example usage
keyword = "monarchy"
plaintext = "instruments"
encrypted_message = playfair_encrypt_visualize(plaintext, keyword)
print("Encrypted message:", encrypted_message)

# %%
