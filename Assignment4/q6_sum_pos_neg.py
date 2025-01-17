def sum_positive_negative(numbers):
    positive_sum = 0
    negative_sum = 0
    
    for num in numbers:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_sum += num
    
    print(f"Sum of positive numbers: {positive_sum}")
    print(f"Sum of negative numbers: {negative_sum}")


numbers = [10, -20, 30, -40, 50]
sum_positive_negative(numbers)
