over_time_rate = 12.00

for i in range(1, 11):
    total_hours = int(input(f"Enter the total hours for employee {i}: "))
    if(total_hours > 40):
        over_time_pay = (total_hours - 40)*over_time_rate
        print(f"Overtime payment for employee {i} is Rs. {over_time_pay}")
    else:
        print("Not worked overtime!")