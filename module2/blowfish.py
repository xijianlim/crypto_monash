# pip install pycrypto

from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

BLOCK_SIZE = 8  # Blowfish block size is 8 bytes (64 bits)

# Function to encrypt plaintext using Blowfish
def blowfish_encrypt(plaintext, key):
    # Ensure key length is between 4 and 56 bytes
    if len(key) < 4 or len(key) > 56:
        raise ValueError("Key must be between 4 and 56 bytes long.")
    
    # Create a Blowfish cipher object
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    
    # Pad the plaintext to be a multiple of BLOCK_SIZE (8 bytes)
    padded_text = pad(plaintext.encode('utf-8'), BLOCK_SIZE)
    
    # Encrypt the padded plaintext
    ciphertext = cipher.encrypt(padded_text)
    
    return ciphertext

# Function to decrypt ciphertext using Blowfish
def blowfish_decrypt(ciphertext, key):
    # Ensure key length is between 4 and 56 bytes
    if len(key) < 4 or len(key) > 56:
        raise ValueError("Key must be between 4 and 56 bytes long.")
    
    # Create a Blowfish cipher object
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    
    # Decrypt the ciphertext
    decrypted_padded_text = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted plaintext to get the original message
    decrypted_text = unpad(decrypted_padded_text, BLOCK_SIZE).decode('utf-8')
    
    return decrypted_text

# Example usage
if __name__ == "__main__":
    # Example key (between 4 and 56 bytes long)
    key = b'SuperSecretKey'

    # Example plaintext
    plaintext = "This is a secret message"
    print(f"Plaintext: {plaintext}")

    # Encrypt the plaintext
    ciphertext = blowfish_encrypt(plaintext, key)
    print(f"Ciphertext (in bytes): {ciphertext}")

    # Decrypt the ciphertext
    decrypted_text = blowfish_decrypt(ciphertext, key)
    print(f"Decrypted text: {decrypted_text}")
