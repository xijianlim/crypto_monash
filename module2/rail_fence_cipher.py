# %%
import plotly.graph_objects as go

def rail_fence_cipher(text, key):
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    padded_text = text.ljust(num_rows * num_cols, '_')
    grid = [list(padded_text[i * num_cols: (i + 1) * num_cols]) for i in range(num_rows)]
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    encrypted_text = ''.join(''.join(grid[row][col] for row in range(num_rows)) for col in key_order)
    return encrypted_text.replace('_', '')

def rail_fence_decrypt(encrypted_text, key, original_length):
    num_cols = len(key)
    num_rows = (original_length + num_cols - 1) // num_cols
    col_lengths = [num_rows] * num_cols
    extra_chars = num_rows * num_cols - original_length
    for i in range(extra_chars):
        col_lengths[-(i + 1)] -= 1
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    columns = {}
    start = 0
    for index in key_order:
        length = col_lengths[index]
        columns[index] = list(encrypted_text[start:start + length])
        start += length
    decrypted_text = ''
    for row in range(num_rows):
        for col in range(num_cols):
            if columns[col]:
                decrypted_text += columns[col].pop(0)
    return decrypted_text.strip('_')

def plot_grid(grid, key_order, title, show_key=True):
    num_rows = len(grid)
    num_cols = len(grid[0]) if grid else 0
    fig = go.Figure()

    # Plot the key labels at the top
    if show_key:
        for i, col in enumerate(key_order):
            fig.add_annotation(
                x=col, y=num_rows,  # Place above the grid
                text=key[col],
                showarrow=False,
                font=dict(color="black", size=14),
                align="center",
            )

    # Plot each cell in the grid with the characters
    for row in range(num_rows):
        for col in range(num_cols):
            cell_text = grid[row][col]
            fig.add_annotation(
                x=col, y=num_rows - row - 1,
                text=cell_text,
                showarrow=False,
                font=dict(color="blue" if cell_text != '_' else "grey", size=14),
                align="center",
            )

    fig.update_layout(
        title=title,
        xaxis=dict(showgrid=False, zeroline=False, tickvals=[], range=[-0.5, num_cols - 0.5]),
        yaxis=dict(showgrid=False, zeroline=False, tickvals=[], range=[-0.5, num_rows + 0.5]),
        width=400,
        height=400,
    )

    fig.show()

def create_encryption_grid(text, key):
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols
    padded_text = text.ljust(num_rows * num_cols, '_')
    return [list(padded_text[i * num_cols: (i + 1) * num_cols]) for i in range(num_rows)]

def create_decryption_grid(decrypted_text, num_rows, num_cols):
    grid = [list(decrypted_text[i * num_cols: (i + 1) * num_cols]) for i in range(num_rows)]
    return grid

# Example usage
text = "oneringtorulethemall"
key = "25413"

# Encrypt and plot the encrypted grid
encrypted_message = rail_fence_cipher(text, key)
print("Encrypted message:", encrypted_message)
encryption_grid = create_encryption_grid(text, key)
key_order = sorted(range(len(key)), key=lambda k: key[k])
plot_grid(encryption_grid, key_order, "Encryption Grid with Key")

# Decrypt and plot the decrypted grid
decrypted_message = rail_fence_decrypt(encrypted_message, key, len(text))
print("Decrypted message:", decrypted_message)
num_cols = len(key)
num_rows = (len(text) + num_cols - 1) // num_cols
decryption_grid = create_decryption_grid(decrypted_message, num_rows, num_cols)
plot_grid(decryption_grid, key_order, "Decryption Grid", show_key=False)

# %%
