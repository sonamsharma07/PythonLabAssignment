basic_salary = int(input("Enter the basic salary: "))
DA = (basic_salary * 40)//100 
HRA = (basic_salary * 20)//100

gross_salary = basic_salary + DA + HRA
  
print(f"Dearness Allowance is {DA}")
print(f"House Rent Allowance is {HRA}")
print(f"Gross salary is: {gross_salary}")