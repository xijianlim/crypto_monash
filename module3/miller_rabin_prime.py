import random

def is_prime_miller_rabin(n, k=5):
    """
    Miller-Rabin Primality Test.
    
    Parameters:
    n : int - The number to test for primality.
    k : int - The number of iterations (more iterations increase accuracy).
    
    Returns:
    bool - True if n is likely prime, False if n is composite.
    """
    # Handle small cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n - 1 as 2^s * d
    s = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        s += 1
    
    # Perform the test k times
    for _ in range(k):
        # Pick a random base a in the range [2, n - 2]
        a = random.randint(2, n - 2)
        
        # Compute a^d % n
        x = pow(a, d, n)
        
        # If x is 1 or n - 1, continue to next iteration
        if x == 1 or x == n - 1:
            continue
        
        # Check powers of x
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            # If no x == n - 1 was found, n is composite
            return False
    
    # If no evidence of compositeness was found, n is probably prime
    return True

# Example usage
n = 2111
print(f"{n} is prime: {is_prime_miller_rabin(n)}")