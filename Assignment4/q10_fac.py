number = int(input("Enter a number: "))

def factorial(n):
    if n < 0:
        return "Invalid!"
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(number)
print(f"The factorial of {number} is: {f}")