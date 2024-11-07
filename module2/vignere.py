# %%
def vigenere_encrypt(plaintext, key, mode='encrypt'):
    # Define helper function to convert letter to number (A=0, B=1, ..., Z=25)
    def letter_to_num(letter):
        return ord(letter.upper()) - ord('A')

    # Define helper function to convert number to letter (0=A, 1=B, ..., 25=Z)
    def num_to_letter(num):
        return chr(num + ord('A'))
    
    # Prepare the key by repeating it to match the length of the plaintext
    key_repeated = (key * ((len(plaintext) // len(key)) + 1))[:len(plaintext)]
    
    ciphertext = []
    
    # Encrypt each character
    for p_char, k_char in zip(plaintext, key_repeated):
        p_num = letter_to_num(p_char)
        k_num = letter_to_num(k_char)
        if mode == 'encrypt':
            c_num = (p_num + k_num) % 26
        else:
            c_num = (p_num - k_num) % 26  # Cipher formula: (P + K) mod 26
        ciphertext.append(num_to_letter(c_num))
    
    return ''.join(ciphertext)

# Example usage
plaintext = "wearediscoveredsaveyourself"
key = "deceptive"

ciphertext = vigenere_encrypt(plaintext, key, mode='encrypt')
print(ciphertext)

decrypted = vigenere_encrypt(ciphertext, key, mode='decrypt')
print(decrypted)
# %%
