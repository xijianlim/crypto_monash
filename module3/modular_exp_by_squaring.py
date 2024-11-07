# %%
def modular_exponentiation_by_squaring(a, b, m):
    print(f"Calculating {a}^{b} mod {m}\n")

    # Initial values
    base = a % m  # Reduce base mod m
    exponent = b
    result = 1  # Initialize result to 1 for modular multiplication
    step = 1

    # Step-by-step calculation using exponentiation by squaring
    while exponent > 0:
        # Print the current value of the exponent
        print(f"Step {step}: Current exponent = {exponent}")
        print(f"current base: {base}")

        
        # If the current exponent bit is 1, multiply the result by the current base
        if exponent % 2 == 1:
            print(f"  result = (result * base) mod m")
            print(f"  = ({result} * {base}) mod {m} = {(result * base) % m}")
            result = (result * base) % m

        # Square the base and print the updated formula for the base
        print(f"  base = (base * base) mod m")
        print(f"  = ({base} * {base}) mod {m} = {(base * base) % m}")
        base = (base * base) % m

        # Update exponent by halving it (right shift)
        exponent //= 2
        step += 1

    print(f"\nFinal result: {a}^{b} mod {m} = {result}")
    return result

# Example usage
modular_exponentiation_by_squaring(14, 27, 55)

# %%
