cp = float(input("Enter the cost price of the item: "))
sp = float(input("Enter the selling price of the item: "))

if sp > cp:
    profit = sp - cp
    print(f"The seller made a profit of: {profit}")
elif sp < cp:
    loss = cp - sp
    print(f"The seller incurred a loss of: {loss}")
else:
    print("The seller neither made a profit nor incurred a loss. The selling price is equal to the cost price.")
