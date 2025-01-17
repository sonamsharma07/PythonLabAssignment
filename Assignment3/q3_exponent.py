base = int(input("Enter first number: "))
exponent = int(input("Enter second number: "))

def calculate_power(base, exponent):
    return base**exponent

result = calculate_power(base, exponent)
print(f"{base} to the power {exponent} is equal to: {result}")
