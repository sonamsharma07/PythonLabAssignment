num = int(input("Enter a number: "))

if num < 0:
    abs_value = num * (-1)
else:
    abs_value = num

print(f"The absolute value of {num} is {abs_value}")
