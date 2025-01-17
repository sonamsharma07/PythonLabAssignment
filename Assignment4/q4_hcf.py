first_no = int(input("Enter first number: "))
second_no = int(input("Enter second number: "))

def find_HCF(no1, no2):
    while no2 != 0:  
        no1, no2 = no2, no1 % no2  
    return no1

HCF = find_HCF(first_no, second_no)
print("HCF of two numbers is:", HCF)



