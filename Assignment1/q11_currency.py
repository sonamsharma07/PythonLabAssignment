total_amount = int(input("Enter the total amount to be withdrawn (in hundreds): "))
note_100 = 0
note_50 = 0
note_10 = 0

note_100 = total_amount // 100
total_amount = total_amount % 100 

note_50 = total_amount // 50
total_amount = total_amount % 50  

note_10 = total_amount // 10
total_amount = total_amount % 10  


print(f"Total 100 notes: {note_100}")
print(f"Total 50 notes: {note_50}")
print(f"Total 10 notes: {note_10}")
