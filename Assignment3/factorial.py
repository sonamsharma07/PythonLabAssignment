number = int(input("Enter a number: "))

def calculate_factorial(number):
    if number<0:
        print("Factorial is not calculated on negative numbers!")
    else:
        factorial = 1
        for i in range(2,number+1):
            factorial *= i 
        
        return factorial

factorial = calculate_factorial(number)
print(f"The factorial of {number} is: {factorial}")