# %%
def rail_fence_cipher(text, key):
    # Determine the number of rows based on the length of the text and key length
    num_cols = len(key)
    num_rows = (len(text) + num_cols - 1) // num_cols  # Round up to cover all characters

    # Pad the text to fill the grid completely
    padded_text = text.ljust(num_rows * num_cols, '_')

    # Step 1: Fill the grid row by row
    grid = [list(padded_text[i * num_cols: (i + 1) * num_cols]) for i in range(num_rows)]

    # Step 2: Reorder columns based on the key with "1" as the first column
    key_order = sorted(range(len(key)), key=lambda k: key[k])  # Sorting key positions based on key order

    # Step 3: Create the encrypted text by reading columns in the specified order
    encrypted_text = ''.join(''.join(grid[row][col] for row in range(num_rows)) for col in key_order)

    # Remove padding characters
    encrypted_text = encrypted_text.replace('_', '')

    return encrypted_text

# Example usage
text = "oneringtorulethemall"
key = "25413"
encrypted_message = rail_fence_cipher(text, key)
print("Encrypted message:", encrypted_message)

# %%
