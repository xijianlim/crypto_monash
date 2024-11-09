# %%
def caesar_cipher_encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Only shift alphabetic characters
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabet characters are added as is
    return encrypted_text

def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Only shift alphabetic characters
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabet characters are added as is
    return decrypted_text

# Example usage
plaintext = "oneringtorulethemall"
shift = 23

# Encrypt the plaintext
encrypted_message = caesar_cipher_encrypt(plaintext, shift)
print("Encrypted message:", encrypted_message)

# Decrypt the ciphertext
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)

# %%
