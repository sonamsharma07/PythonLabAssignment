def find_range(numbers):
    min = find_min(numbers)  
    max = find_max(numbers)   
    range_value = max - min  
    return range_value

def find_min(numbers):
    min = numbers[0]
    length = len(numbers)
    for i in range(length):
        if numbers[i] < min:
            min = numbers[i]
        
    return min

def find_max(numbers):
    max = numbers[0]
    length = len(numbers)
    for i in range(length):
        if numbers[i] > max:
            max = numbers[i]
        
    return max

numbers = [10, 20, 30, 40, 50]  
print("List:", numbers)
number_range = find_range(numbers)
print(f"Range: {number_range}")
