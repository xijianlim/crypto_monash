# %%
# Extended Euclidean Algorithm to solve for x and b
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

# Solving for gcd(1914, 899)
a = 1914
b = 899
gcd_result, x, y = extended_gcd(a, b)

gcd_result, x, y
# %%

# %%
# Extended Euclidean Algorithm with detailed steps and substitutions

def extended_euclidean_algorithm_with_substitutions(a, b):
    steps = []
    substitutions = []

    # Step 1: Euclidean Algorithm steps to find the GCD
    def euclidean_steps(a, b):
        while b != 0:
            quotient = a // b
            remainder = a % b
            steps.append((a, b, quotient, remainder))
            a, b = b, remainder

    # Step 2: Extended Euclidean Algorithm with back-substitution
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

    # Step 3: Perform the Euclidean algorithm steps
    euclidean_steps(a, b)

    # Step 4: Perform the extended Euclidean algorithm to find coefficients
    gcd, x, y = extended_gcd(a, b)

    # Step 5: Print out the Euclidean algorithm steps
    for a, b, quotient, remainder in steps:
        print(f"{a} = {quotient} * {b} + {remainder}")

    # Step 6: Start the substitution process from the last non-zero remainder
    print("\nBack-Substitution Process:")
    last_gcd = steps[-2][3]  # The last non-zero remainder is the GCD
    substitutions.append(f"{last_gcd} = {steps[-2][0]} - {steps[-2][2]} * {steps[-2][1]}")

    for i in range(len(steps) - 3, -1, -1):
        a, b, quotient, remainder = steps[i]
        prev_a, prev_b, prev_quotient, prev_remainder = steps[i + 1]
        substitution = substitutions[-1].replace(f"{prev_remainder}", f"({prev_a} - {prev_quotient} * {prev_b})")
        substitutions.append(substitution)
        print(substitutions[-1])

    # Final substitution step with the equation
    print(f"\nFinal result: {gcd} = {x} * {steps[0][0]} + {y} * {steps[0][1]}")

    # Print final coefficients
    print(f"The GCD of {steps[0][0]} and {steps[0][1]} is: {gcd}")
    print(f"Coefficients: x = {x}, y = {y}")
    print(f"Equation: {steps[0][0]} * ({x}) + {steps[0][1]} * ({y}) = {gcd}")

# Example usage with a = 1914, b = 899
a = 1914
b = 899
extended_euclidean_algorithm_with_substitutions(a, b)



# %%
a = 1180
b = 482
extended_euclidean_algorithm_with_substitutions(a, b)

# %%
