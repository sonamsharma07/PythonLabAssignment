days_late = int(input("Enter the number of days the book is late: "))

if days_late <= 0:
    print("The book is returned on time. No fine.")

elif days_late <= 5:
    fine = days_late * 0.50  
    print(f"The fine is {fine} paise.")

elif days_late <= 10:
    fine = (days_late - 5) * 1.00 + (5 * 0.50) 
    print(f"The fine is {fine} rupees.")

elif days_late <= 30:
    fine = (days_late - 10) * 5.00 + (5 * 1.00) + (5 * 0.50) 
    print(f"The fine is {fine} rupees.")
    
else:
    print("Your membership has been cancelled due to late return after 30 days.")
