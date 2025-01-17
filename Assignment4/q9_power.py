a = int(input("Enter the base number: "))
b = int(input("Enter the exponent: "))

def power(a, b):
    return a ** b

result = power(a, b)

print(f"{a} raised to the power {b} is equal to: {result}")
