# %%
import math

# Function to check if two numbers are relatively prime
def are_relatively_prime(a, b):
    return math.gcd(a, b) == 1

# List all numbers less than n that are relatively prime to n
def relatively_prime_to(n):
    return [i for i in range(1, n) if are_relatively_prime(i, n)]

# Example usage: numbers less than 35 that are relatively prime to 35
n = 35
numbers_rel_prime_to_n = relatively_prime_to(n)
print(numbers_rel_prime_to_n)
print(len(numbers_rel_prime_to_n))
# %%

n = 37
numbers_rel_prime_to_n = relatively_prime_to(n)
print(numbers_rel_prime_to_n)
print(len(numbers_rel_prime_to_n))
# %%



from math import gcd

def modular_exponentiation_with_totient(base, exponent, modulus):
    """
    Calculates base^exponent % modulus using Euler's Totient to simplify when possible.
    
    Parameters:
    base (int): The base number.
    exponent (int): The exponent.
    modulus (int): The modulus.
    
    Returns:
    int: Result of base^exponent % modulus.
    """
    # Step 1: Calculate Euler's Totient for the modulus
    def euler_totient(n):
        count = 0
        for i in range(1, n):
            if gcd(n, i) == 1:
                count += 1
        return count

    # Calculate the totient of the modulus
    totient = euler_totient(modulus)
    
    # Step 2: Reduce the exponent using the totient if gcd(base, modulus) == 1
    if gcd(base, modulus) == 1:
        reduced_exponent = exponent % totient
    else:
        reduced_exponent = exponent  # Use the full exponent if gcd(base, modulus) != 1

    # Step 3: Compute the result
    result = pow(base, reduced_exponent, modulus)
    return result

# Example usage
base = 7
exponent = 133
modulus = 26
result = modular_exponentiation_with_totient(base, exponent, modulus)
print(f"The result of {base}^{exponent} % {modulus} using Euler's Totient is {result}")
# %%
