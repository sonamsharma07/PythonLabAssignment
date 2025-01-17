orignal_no = int(input("Enter a five-digit number: "))
temp_no = orignal_no
reversed_no = 0

while temp_no > 0:
    rem = temp_no % 10  
    reversed_no = reversed_no * 10 + rem  
    temp_no //= 10 

if orignal_no == reversed_no:
    print(f"The original number {orignal_no} is equal to the reversed number {reversed_no}.")
else:
    print(f"The original number {orignal_no} is not equal to the reversed number {reversed_no}.")
