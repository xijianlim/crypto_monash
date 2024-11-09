# %%
def create_playfair_grid(keyword):
    # Remove duplicate letters and combine 'I' and 'J'
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    keyword = "".join(dict.fromkeys(keyword.upper().replace("J", "I")))  # Removes duplicates
    grid_letters = keyword + "".join([ch for ch in alphabet if ch not in keyword])
    
    # Create 5x5 grid
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
    # If length is odd, add 'Z' at the end as padding
    if len(plaintext) % 2 != 0:
        pairs[-1] = pairs[-1][0] + 'Z' if len(pairs[-1]) == 1 else pairs[-1]
    return pairs

def encrypt_pair(grid, a, b):
    row_a, col_a = find_position(grid, a)
    row_b, col_b = find_position(grid, b)
    
    if row_a == row_b:
        # Same row: move right
        encrypted_a = grid[row_a][(col_a + 1) % 5]
        encrypted_b = grid[row_b][(col_b + 1) % 5]
    elif col_a == col_b:
        # Same column: move down
        encrypted_a = grid[(row_a + 1) % 5][col_a]
        encrypted_b = grid[(row_b + 1) % 5][col_b]
    else:
        # Rectangle swap
        encrypted_a = grid[row_a][col_b]
        encrypted_b = grid[row_b][col_a]
    
    return encrypted_a + encrypted_b

def playfair_encrypt(plaintext, keyword):
    grid = create_playfair_grid(keyword)
    pairs = prepare_text(plaintext)
    encrypted_text = "".join(encrypt_pair(grid, a, b) for a, b in pairs)
    return encrypted_text

# Example usage
keyword = "monarchy"
plaintext = "instruments"
encrypted_message = playfair_encrypt(plaintext, keyword)
print("Encrypted message:", encrypted_message)

# %%
