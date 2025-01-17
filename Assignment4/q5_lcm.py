first_no = int(input("Enter the first number: "))
second_no = int(input("Enter the second number: "))

def find_lcm(x, y):
    if x == 0 or y == 0:
        return 0
    if x > y:
        max = x
        min = y
    else:
        max = y
        min = x
    if max%min ==  0:
        return max
    else:
        i = 2
        while True:
            lcm = max*i
            if lcm%min == 0:
                return lcm
            i = i+1

result = find_lcm(first_no, second_no)
print(f"The LCM of {first_no} and {second_no} is {result}")
