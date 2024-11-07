# %%
def prime_factors(n):
    """
    This function calculates the prime factors of a given number n.
    
    Parameters:
    n (int): The number to calculate prime factors for.
    
    Returns:
    list: A list of prime factors of the number n.
    """
    factors = []
    
    # Step 1: Divide n by 2 until it's odd
    while n % 2 == 0:
        factors.append(2)
        print(2)
        n = n // 2
    
    # Step 2: Divide n by odd numbers starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            print(i)
            factors.append(i)
            n = n // i
    
    # Step 3: If n is a prime number greater than 2, add it to the factors
    if n > 2:
        print(n)
        factors.append(n)
    
    return factors

# Example usage
number = 3000
factors = prime_factors(number)
print(f"Prime factors of {number}: {factors}")


# %%
import math

math.gcd(300,18)
math.gcd(54,24)
# %%
math.gcd(54,24)
# %%

(12+7)%6
# %%

(12*5)%6
# %%
3%5
# %%
9%5
# %%


## Using Fermat's theorem, prove that a^p ≡ a (mod p) for any integer a and any prime number p.

# a^p = a (mod p)
# if a =3 and p = 5

# since a^p == 3^5
# lets break down 3^5 into two parts: 3^2 and 3^3
# a^p =[(3^2 mod 5) * (3^3 mod 5)] mod 5
# then a^p =[(9 mod 5) * (27 mod 5)] mod 5

# since 9 mod 5 = 4 and 27 mod 5 = 2 ->
# a^p =[(4 mod 5) * (2 mod 5)] mod 5
# a^p =(4 *2)  mod 5
# a^p =(8) mod 5

# since 8 mod 5 = 3 ->
# a^p = 3 mod 5
# therefore a^p ≡ 3 (mod 5) and a^p ≡ a (mod p) for any integer a and any prime number p.





### 
# %%
def is_prime_fermat(n, a=2):
    """
    Function to test whether n is prime using Fermat's theorem with the given fact.
    Arguments:
    n -- the number to test for primality
    a -- the integer to use for the test (default is 2)
    Returns:
    True if n is likely prime, False if n is composite.
    """
    # Step 1: Express n-1 as 2^s * r, where r is odd
    s = 0
    r = n - 1
    while r % 2 == 0:
        r //= 2
        s += 1
    print(f"r = {r}, s = {s}")
    # Step 2: Compute a^r mod n
    ar_mod_n = pow(a, r, n)
    
    # Step 3: If a^r mod n is 1, n is likely prime
    if ar_mod_n == 1:
        return True

    # Step 4: Compute a^(2^j * r) mod n for j = 0, 1, ..., s-1
    for j in range(s):
        # Compute a^(2^j * r) mod n
        a2jr_mod_n = pow(a, 2**j * r, n)
        if a2jr_mod_n == n - 1:
            return True

    # If none of the conditions are satisfied, n is composite
    return False

# Test the function for n = 101
n = 101
result = is_prime_fermat(n)
result
# %%
import math
## Running test
a=[2,3,5,7]
for i in a:
    if math.gcd(i,101) == 1:
        print(f"is_prime_fermat(101,{i})")
# %%
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
        print(f"checking if using {a}")
        
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
# %%
