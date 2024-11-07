# %%
 def extended_euclidean(a, b):
    """
    Returns the greatest common divisor of a and b, along with the coefficients
    (x, y) such that a * x + b * y = gcd(a, b).
    """
    # Base case: if b is 0, gcd is a, and the coefficients are (1, 0)
    if b == 0:
        return a, 1, 0
    
    # Recursive case
    gcd, x1, y1 = extended_euclidean(b, a % b)
    
    # Update coefficients for the current step
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

def modular_inverse(a, m):
    """
    Returns the modular inverse of a modulo m, if it exists.
    If a and m are coprime (gcd(a, m) == 1), the modular inverse exists and
    this function returns it. Otherwise, it returns None.
    """
    gcd, x, _ = extended_euclidean(a, m)
    
    # Modular inverse exists only if gcd(a, m) is 1
    if gcd != 1:
        return None  # Inverse does not exist
    
    # Ensure the result is positive by taking x % m
    return x % m

# Example usage
a = 7
m = 26
inverse = modular_inverse(a, m)
if inverse is not None:
    print(f"The modular inverse of {a} modulo {m} is {inverse}")
else:
    print(f"No modular inverse exists for {a} modulo {m}")

# %%
