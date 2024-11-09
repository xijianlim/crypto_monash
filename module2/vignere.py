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
    print("Key (repeated):", key_repeated)
    
    plaintext_numerical = [letter_to_num(p) for p in plaintext]
    key_numerical = [letter_to_num(k) for k in key_repeated]
    
    print("Plaintext (numerical):", plaintext_numerical)
    print("Key (numerical):", key_numerical)
    
    ciphertext = []
    
    # Encrypt each character
    for p_char, k_char in zip(plaintext, key_repeated):
        p_num = letter_to_num(p_char)
        k_num = letter_to_num(k_char)
        if mode == 'encrypt':
            c_num = (p_num + k_num) % 26
        else:
            c_num = (p_num - k_num) % 26  # Cipher formula: (P + K) mod 26
        c_char = num_to_letter(c_num)
        ciphertext.append(c_char)
        
        # Print details for each character
        print(f"Plaintext character: {p_char} (number: {p_num}), Key character: {k_char} (number: {k_num}), Ciphertext character: {c_char} (number: {c_num})")
    
    final_ciphertext = ''.join(ciphertext)
    print("Final Ciphertext:", final_ciphertext)
    
    return final_ciphertext


# Example usage
plaintext = "wearediscoveredsaveyourself"
key = "deceptive"

ciphertext = vigenere_encrypt(plaintext, key, mode='encrypt')
print(ciphertext)

decrypted = vigenere_encrypt(ciphertext, key, mode='decrypt')
print(decrypted)
# %%
