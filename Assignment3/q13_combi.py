for i in range(1, 4):     
    for j in range(1, 4): 
        if j != i:        
            for k in range(1, 4): 
                if k != i and k != j: 
                    print(i, j, k)
