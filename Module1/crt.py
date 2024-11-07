# %%
def chinese_remainder_theorem_with_steps_sorted(congruences, moduli):
    """
    Solves the system of congruences using the Chinese Remainder Theorem and prints out each step.
    The system is sorted by the modulus in descending order.

    Parameters:
    congruences (list): List of integers representing the congruences.
    moduli (list): List of integers representing the moduli. The moduli must be pairwise coprime.

    Returns:
    int: The smallest solution to the system of congruences.
    """

    # Sort the moduli and congruences in descending order based on moduli
    sorted_pairs = sorted(zip(moduli, congruences), reverse=True, key=lambda x: x[0])
    sorted_moduli, sorted_congruences = zip(*sorted_pairs)

    # Helper function for extended Euclidean algorithm to find modular inverse
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    # Helper function to find the modular inverse of N_i modulo n_i
    def mod_inverse(N_i, n_i):
        gcd, inverse, _ = extended_gcd(N_i, n_i)
        if gcd == 1:
            return inverse % n_i
        else:
            raise ValueError(f"No modular inverse exists for {N_i} mod {n_i}")

    # Step 1: Calculate the product of all moduli (N = n_1 * n_2 * ... * n_k)
    N = 1
    for n_i in sorted_moduli:
        N *= n_i
    print(f"\nStep 1: Calculate the product of all moduli N = {N}")

    # Step 2: Initialize the solution
    x = 0

    # Step 3: Solve using the formula x = sum(a_i * N_i * y_i), where N_i = N / n_i and y_i is the modular inverse of N_i modulo n_i
    print("\nStep 2: Solve each congruence using the CRT formula:")
    for i in range(len(sorted_congruences)):
        a_i = sorted_congruences[i]
        n_i = sorted_moduli[i]
        N_i = N // n_i  # Partial modulus
        y_i = mod_inverse(N_i, n_i)  # Modular inverse of N_i mod n_i
        term = a_i * N_i * y_i
        print(f"  For x congruent to {a_i} (mod {n_i}):")
        print(f"    N_{i+1} = {N_i}, modular inverse y_{i+1} = {y_i}")
        print(f"    Term = {a_i} * {N_i} * {y_i} = {term}")
        x += term

    # Step 4: Return the solution modulo the product of all moduli
    result = x % N
    print(f"\nStep 3: Compute the final result modulo N = {N}:")
    print(f"  x is congruent to {result} (mod {N})\n")
    return result

# Example usage with the system of congruences:
# x congruent to 1 (mod 3)
# x congruent to 4 (mod 5)
# x congruent to 6 (mod 7)
congruences = [3, 1, 6]
moduli = [5, 7, 8]

# Solve the system using the Chinese Remainder Theorem with detailed steps and sorted moduli
solution = chinese_remainder_theorem_with_steps_sorted(congruences, moduli)
# %%
918/280
# %%
918/3

# %%
