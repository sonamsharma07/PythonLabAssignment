orignal_no = int(input("Enter a five-digit number: "))
temp_no = orignal_no
reversed_no = 0

while temp_no > 0:
    rem = temp_no % 10  
    reversed_no = reversed_no * 10 + rem  
    temp_no //= 10 

print(f"The original number is: {orignal_no}")
print(f"The reversed number is: {reversed_no}")
