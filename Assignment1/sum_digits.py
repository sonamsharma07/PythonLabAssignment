number = int(input("Enter a five-digit number: "))

sum_digit = 0
while number > 0:
    rem = number % 10  
    sum_digit += rem  
    number = number // 10       

print(f"The sum of the digits is: {sum_digit}")
