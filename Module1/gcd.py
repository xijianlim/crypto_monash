# %%

def gcd_euclidean(a, b, steps=None):
    if steps is None:
        steps = []
    if b == 0:
        return a, steps
    steps.append((a, b, a // b, a % b))
    return gcd_euclidean(b, a % b, steps)

def display_gcd_steps(steps):
    for i, (a, b, quotient, remainder) in enumerate(steps):
        print(f"Step {i + 1}: {a} ÷ {b} = {quotient} remainder {remainder}")

    print(f" GCD is {steps[-1][1]}")

# Calculate gcd and steps
gcd_result, steps = gcd_euclidean(1160718174, 316258250)

# Display the steps
display_gcd_steps(steps)
# %%
steps
# %%
