print("Prime numbers between 1 and 300 are: ")

for i in range(2, 301):  
    is_prime = True  
    for j in range(2, i//2 + 1): 
        if i % j == 0:
            is_prime = False
            break  
    if is_prime == False:
        continue 
    print(i, end=" ")
