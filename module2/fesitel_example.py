# Feistel cipher implementation in Python

def feistel_round(L, R, round_key):
    # Simple XOR with the round key for demonstration
    new_L = R
    new_R = [L[i] ^ round_key for i in range(len(L))]
    return new_L, new_R

def feistel_encrypt(plaintext, keys, num_rounds):
    # Split the plaintext into two halves
    print("splitting the plaintext into two halves")
    L, R = plaintext[:len(plaintext)//2], plaintext[len(plaintext)//2:]
    
    print(f"Initial Left: {L}, Initial Right: {R}")
    
    # Perform the encryption rounds
    for i in range(num_rounds):
        print(f"\nRound {i+1}")
        L, R = feistel_round(L, R, keys[i])
        print(f"After round {i+1} -> Left: {L}, Right: {R}")
    
    # Concatenate L and R to form the ciphertext
    ciphertext = L + R
    print(f"\nCiphertext: {ciphertext}")
    return ciphertext

def feistel_decrypt(ciphertext, keys, num_rounds):
    # Split the ciphertext into two halves
    L, R = ciphertext[:len(ciphertext)//2], ciphertext[len(ciphertext)//2:]
    
    print(f"\nDecryption process:")
    print(f"Initial Left: {L}, Initial Right: {R}")
    
    # Perform the decryption rounds (in reverse order)
    for i in range(num_rounds-1, -1, -1):
        print(f"\nRound {num_rounds - i}")
        R, L = feistel_round(R, L, keys[i])
        print(f"After round {num_rounds - i} -> Left: {L}, Right: {R}")
    
    # Concatenate L and R to form the plaintext
    plaintext = L + R
    print(f"\nDecrypted plaintext: {plaintext}")
    return plaintext

# Convert the string to a list of ASCII values
def string_to_ascii(s):
    return [ord(c) for c in s]

# Convert list of ASCII values to a string
def ascii_to_string(ascii_list):
    return ''.join(chr(i) for i in ascii_list)

# Main function
def main():
    plaintext = "hello"
    print(f"Plaintext: {plaintext}")
    
    # Convert plaintext to ASCII for easier manipulation in the cipher
    plaintext_ascii = string_to_ascii(plaintext)
    print(f'ASCII:', plaintext_ascii)
    
    # Number of rounds for the Feistel cipher
    num_rounds = 4
    
    # Generate some simple round keys (these are just numbers for demonstration)
    keys = [i + 1 for i in range(num_rounds)]
    print(f"Keys: {keys}")
    
    # Encrypt the plaintext
    ciphertext_ascii = feistel_encrypt(plaintext_ascii, keys, num_rounds)
    print(f"\nCiphertext ASCII: {''.join(chr(i) for i in ciphertext_ascii)}")
    
    # Decrypt the ciphertext
    decrypted_ascii = feistel_decrypt(ciphertext_ascii, keys, num_rounds)
    
    # Convert ASCII back to string for final output
    decrypted_text = ascii_to_string(decrypted_ascii)
    print(f"\nDecrypted text: {decrypted_text}")

if __name__ == "__main__":
    main()
