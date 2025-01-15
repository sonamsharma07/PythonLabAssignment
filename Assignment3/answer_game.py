count_of_zero = 0
count_of_negative = 0
count_of_positive = 0
answer = 'y'

while(answer == 'y'):
    answer = input("Do you want to enter a number answer in y/n only: ")
    if answer == 'n':
        print("Ok!")
    elif answer == 'y' :
        number = int(input("Enter a number: "))  
        if number == 0:
            count_of_zero += 1 
        elif number < 0:
            count_of_negative += 1 
        elif number > 0:
            count_of_positive += 1
    else :
        print("You have entered a wrong command!")


print("The count of zeroes", count_of_zero)
print("The count of negative numbers", count_of_negative)
print("The count of positive numbers", count_of_positive)