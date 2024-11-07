# %%

import numpy as np
# Function to compute modular inverse of a number modulo m using the Extended Euclidean Algorithm
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to compute the inverse of a 2x2 matrix modulo 26
def matrix_mod_inverse(matrix, mod=26):
    # Ensure the matrix is 2x2
    if matrix.shape != (2, 2):
        raise ValueError("Only 2x2 matrices are supported.")

    # Extract elements from the matrix
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]

    # Compute the determinant
    det = (a * d - b * c) % mod

    # Find the modular inverse of the determinant
    det_inv = mod_inverse(det, mod)
    if det_inv is None:
        raise ValueError("The matrix is not invertible modulo 26.")

    # Compute the adjugate matrix (swapping a <-> d and negating b and c)
    adjugate = np.array([[d, -b], [-c, a]])

    # Multiply the adjugate matrix by the modular inverse of the determinant
    inverse_matrix = (det_inv * adjugate) % mod

    # Ensure all elements are positive by applying mod again if needed
    inverse_matrix = np.mod(inverse_matrix, mod)

    return inverse_matrix

# Example usage:
A = np.array([[5, 8], [17, 3]])

# Compute the inverse of the matrix mod 26
try:
    A_inv = matrix_mod_inverse(A)
    print("Inverse of A mod 26 is:\n", A_inv)
except ValueError as e:
    print(e)
# %%




# Function to decrypt a Hill cipher ciphertext
def hill_cipher_decrypt(ciphertext, matrix, mod=26):
    # Convert letters to numbers (A=0, B=1, ..., Z=25)
    letter_to_num = {chr(i + 65): i for i in range(26)}
    num_to_letter = {i: chr(i + 65) for i in range(26)}
    
    # Convert ciphertext into numerical form
    cipher_numbers = [letter_to_num[char] for char in ciphertext]
    
    # Split the ciphertext numbers into pairs
    pairs = [(cipher_numbers[i], cipher_numbers[i+1]) for i in range(0, len(cipher_numbers), 2)]
    
    # Decrypt each pair using the inverse matrix
    plaintext_numbers = []
    
    for pair in pairs:
        # Convert pair to a column vector
        vector = np.array([[pair[0]], [pair[1]]])
        
        # Multiply by the inverse matrix and apply modulo 26
        enccrypt_decrip_vector = np.dot(matrix, vector) % mod
        enccrypt_decrip_vector = enccrypt_decrip_vector.astype(int)  # Convert to integers
        
        # Append the decrypted values to the plaintext numbers
        plaintext_numbers.append(enccrypt_decrip_vector[0][0])
        plaintext_numbers.append(enccrypt_decrip_vector[1][0])
    
    # Convert numbers back to letters
    plaintext = ''.join(num_to_letter[num] for num in plaintext_numbers)
    
    return plaintext

# Example usage
ciphertext = "MEETMEHERE"
encrypted = 'OIQVOIPBNP'
matrix = np.array([[5, 8], [17, 3]])  # The inverse of A mod 26
inverse_matrix = matrix_mod_inverse(matrix)
# encrypt the ciphertext
encrypted = hill_cipher_decrypt(ciphertext, matrix)
print(f'encrypted: {encrypted}')

#decrypt
decrypted = hill_cipher_decrypt(encrypted, inverse_matrix)
print(f'decrypted: {decrypted}') 




# %%
