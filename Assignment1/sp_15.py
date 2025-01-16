total_sp = float(input("Enter the total selling price of 15 items: "))
total_pro = float(input("Enter the total profit earned on 15 items: "))
total_cp = total_sp - total_pro
cp_one_item = total_cp / 15

print(f"The cost price of one item is: {cp_one_item:.2f}")
