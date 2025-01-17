number = int(input("Enter a number: "))

def calculate_factorial(no):
    if no<0:
        print("Factorial is not calculated on negative number!")
    else:
        f = 1
        for i in range(2,no+1):
            f *= i 
        
        return f

fac = calculate_factorial(no)
print(f"The factorial of {number} is: {fac}")