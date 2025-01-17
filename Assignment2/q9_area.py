l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))

area = l * b
peri = 2 * (l + b)

if area > peri:
    print(f"The area: {area} > The perimeter: {peri}")
else:
    print(f"The perimeter: {peri} > The area: {area}")
