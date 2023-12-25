def logarithm(x, base):
    return logarithm_base(x) / logarithm_base(base)

def logarithm_base(x):
    approx = 0.0001  # Adjust for desired precision
    n = 1.0
    result = 0.0

    while n < x:
        result += approx
        n *= (1 + approx)

    return result

# Take input from the user
x = float(input("Enter the number: "))
base = float(input("Enter the base: "))

# Calculate and print the result
result = logarithm(x, base)
print(f"The logarithm base {base} of {x} is approximately {result}")