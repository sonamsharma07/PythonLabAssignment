number = int(input("Enter a number: "))
new_number = number
sum_of_cubes = 0
while(new_number>0):
    remainder = new_number % 10
    cube_of_remainder = remainder**3
    sum_of_cubes = sum_of_cubes + cube_of_remainder
    new_number = new_number // 10

print(f"Old number = {number}")
print(f"After the operation New number = {sum_of_cubes}")

if sum_of_cubes == number:
    print("The number is an armstrong number!")
else:
    print("The number is not an armstrong number!")
