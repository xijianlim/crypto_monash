# %%

# Function to convert a letter to its alphabetical index (A=0, B=1, ..., Z=25)
def letter_to_index(letter):
    if letter.isupper():
        return ord(letter) - ord('A')
    return ord(letter) - ord('a')

# Function to convert an alphabetical index back to a letter
def index_to_letter(index, is_uppercase):
    if is_uppercase:
        return chr(index + ord('A'))
    return chr(index + ord('a'))

# Function to repeat the key to match the length of the plaintext
def repeat_key(key, length):
    return (key * ((length // len(key)) + 1))[:length]

# Encryption function (Vernam Cipher using only alphabets)
def vernam_encrypt_alphabet(plaintext, key):
    # Prepare the key to match the length of the plaintext
    key_repeated = repeat_key(key, len(plaintext))
    
    ciphertext = []

    # Encrypt by shifting letters according to the key
    for p_char, k_char in zip(plaintext, key_repeated):
        if p_char.isalpha():  # Only encrypt alphabetic characters
            is_upper = p_char.isupper()
            p_index = letter_to_index(p_char)
            k_index = letter_to_index(k_char)
            # Shift plaintext character by key character (mod 26 for alphabet)
            encrypted_index = (p_index + k_index) % 26
            ciphertext.append(index_to_letter(encrypted_index, is_upper))
        else:
            ciphertext.append(p_char)  # Keep non-alphabetic characters unchanged
    
    return ''.join(ciphertext)

# Decryption function (Vernam Cipher using only alphabets)
def vernam_decrypt_alphabet(ciphertext, key):
    # Prepare the key to match the length of the ciphertext
    key_repeated = repeat_key(key, len(ciphertext))
    
    decrypted_text = []

    # Decrypt by reversing the shift using the key
    for c_char, k_char in zip(ciphertext, key_repeated):
        if c_char.isalpha():  # Only decrypt alphabetic characters
            is_upper = c_char.isupper()
            c_index = letter_to_index(c_char)
            k_index = letter_to_index(k_char)
            # Reverse shift ciphertext character by key character (mod 26)
            decrypted_index = (c_index - k_index) % 26
            decrypted_text.append(index_to_letter(decrypted_index, is_upper))
        else:
            decrypted_text.append(c_char)  # Keep non-alphabetic characters unchanged
    
    return ''.join(decrypted_text)

# Example usage with the key "MONEY"
plaintext = "hello"  # Mixed case to show case sensitivity
key = "MONEY"  # Fixed key

# Encrypt the plaintext
ciphertext = vernam_encrypt_alphabet(plaintext, key)
print(f"Encrypted text: {ciphertext}")

# Decrypt the ciphertext
decrypted_text = vernam_decrypt_alphabet(ciphertext, key)
print(f"Decrypted text: {decrypted_text}")

# %%
