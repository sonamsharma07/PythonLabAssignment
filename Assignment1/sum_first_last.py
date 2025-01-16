number = int(input("Enter a four-digit number: "))
last_digit = number % 10

while number > 9:
    number =  number // 10  

first_digit = number
sum_digit = first_digit + last_digit

print(f"The sum of the first digit({first_digit}) and last digit({last_digit}) is: {sum_digit}")
