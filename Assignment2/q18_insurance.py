health = input("Enter the health status (excellent/poor): ").lower()
age = int(input("Enter the age of the person: "))
location = input("Enter the location (city/village): ").lower()
sex = input("Enter the sex (male/female): ").lower()

if health == "excellent" and 25 <= age <= 35 and location == "city" and sex == "male":
    premium_rate = 4
    max_amount = 200000
    print(f"The person should be insured. Premium rate is Rs. {premium_rate} per thousand. Maximum policy amount is Rs. {max_amount}.")

elif health == "excellent" and 25 <= age <= 35 and location == "city" and sex == "female":
    premium_rate = 3
    max_amount = 100000
    print(f"The person should be insured. Premium rate is Rs. {premium_rate} per thousand. Maximum policy amount is Rs. {max_amount}.")

elif health == "poor" and 25 <= age <= 35 and location == "village" and sex == "male":
    premium_rate = 6
    max_amount = 10000
    print(f"The person should be insured. Premium rate is Rs. {premium_rate} per thousand. Maximum policy amount is Rs. {max_amount}.")

else:
    print("The person is not insured.")
