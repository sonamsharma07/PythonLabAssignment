number = int(input("Enter a number: "))

def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is an even number!")
    else:
        print(f"{number} is an odd number!")

check_even_odd(number)