number = input("Enter a five-digit number: ")
new_no = ""

for no in number:
    new_dig = str((int(no) + 1) % 10)
    new_no += new_dig

print(f"The new number obtained is: {new_no}")
