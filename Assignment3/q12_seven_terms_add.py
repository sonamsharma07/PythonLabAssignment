def fac(n):
    f = 1
    for i in range(2,n+1):
        f *= i
    return f 
        
def add_series():
    sum = 0
    for i in range(1, 8):
        sum += i/fac(i)
    return sum
    
sum = add_series()
print(f"Sum of first seven terms: {sum:.4f}")