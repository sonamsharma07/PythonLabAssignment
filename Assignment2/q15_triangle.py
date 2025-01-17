s1 = int(input("Enter the first side of the triangle: "))
s2 = int(input("Enter the second side of the triangle: "))
s3 = int(input("Enter the third side of the triangle: "))

if (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")
