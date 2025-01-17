l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
r = int(input("Enter the radius of the circle: "))

rec_area = l * b
rec_peri = 2 * (l + b)
cir_area = 3.14 * r ** 2
cir_circum = 2 * 3.14 * r

print(f"Area of Rectangle: {rec_area}")
print(f"Perimeter of Rectangle: {rec_peri}")
print(f"Area of Circle: {cir_area}")
print(f"Circumference of Circle: {cir_circum}")