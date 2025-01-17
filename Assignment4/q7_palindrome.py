number = int(input("Enter a number to check palindrome: "))

def check_palindrome(no):
    reversed_no = reverse_number(no)
    if no == reversed_no:
        print(f"Yes, {no} is a palindrome number!")
    else:
        print(f"No, {no} is not a palindrome number!")

def reverse_number(no):
    rev_no = 0
    while no > 0:
        rem = no % 10  
        rev_no = rev_no * 10 + rem  
        no //= 10 
    return rev_no

check_palindrome(number)