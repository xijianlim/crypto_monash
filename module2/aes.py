from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def aes_encrypt_decrypt_java_compatible(message, key, operation='encrypt'):
    """
    Function to encrypt or decrypt a message using AES encryption (AES/ECB/PKCS5PADDING)
    that is compatible with Java's AES encryption.

    :param message: The input message to encrypt or decrypt
    :param key: The secret key used for encryption/decryption (16 bytes for AES-128)
    :param operation: Specify 'encrypt' or 'decrypt' for the desired operation
    :return: Encrypted or decrypted message
    """
    key = key[:16].encode('utf-8')  # Truncate the key to 16 bytes
    cipher = AES.new(key, AES.MODE_ECB)  # Using AES in ECB mode with PKCS5 Padding

    if operation == 'encrypt':
        padded_message = pad(message.encode(), AES.block_size)  # PKCS5 Padding
        encrypted_message = cipher.encrypt(padded_message)
        return base64.b64encode(encrypted_message).decode('utf-8')

    elif operation == 'decrypt':
        encrypted_message = base64.b64decode(message)
        decrypted_message = cipher.decrypt(encrypted_message)
        return unpad(decrypted_message, AES.block_size).decode('utf-8')

# Example Usage
encrypted_message = aes_encrypt_decrypt_java_compatible("howtodoinjava.com", "ssshhhhhhhhhhh!!!!", 'encrypt')
decrypted_message = aes_encrypt_decrypt_java_compatible(encrypted_message, "ssshhhhhhhhhhh!!!!", 'decrypt')

print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)
