n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r(less than n): "))

def calculate_combinatoric(n, r):
    if r > n:
        print("r cannot be greater than n")
        return
    else:
        ncr = cal_factorial(n) // (cal_factorial(r) * cal_factorial(n-r))
        print("Combinatoric C(n, r):", ncr)

def cal_factorial(x):
    fac = 1
    for i in range(2, x+1):
        fac = fac*i
    return fac

calculate_combinatoric(n, r)