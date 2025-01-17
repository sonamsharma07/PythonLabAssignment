s1 = int(input("Enter the first side of the triangle: "))
s2 = int(input("Enter the second side of the triangle: "))
s3 = int(input("Enter the third side of the triangle: "))

def sort_side(s):
    n = len(s)
    for i in range(n-1):
        for j in range(n-1-i):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s

def type_triangle():
    if (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2):
        if s1 == s2 == s3:
            print("The triangle is equilateral!")
    
        elif s1 == s2 or s2 == s3 or s3 == s1:
            print("The triangle is isosceles!")
    
        else:
            print("The triangle is scalene!")
        
        s = [s1, s2, s3]
        ss = sort_side(s)
        if ss[0]**2 + ss[1]**2 == ss[2]**2:
            print("The triangle is a right-angled triangle.")
    else:
        print("The given sides do not form a valid triangle.")

type_triangle()