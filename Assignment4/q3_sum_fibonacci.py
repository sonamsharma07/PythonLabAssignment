terms = int(input("Enter the no of terms: "))

def sum_fibonacci(terms):
    first_term = 0
    second_term = 1
    sum = first_term + second_term

    print("Fibonacci terms: ", first_term, end =" ")
    print(second_term, end =" ")

    for i in range(2, terms):
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term
        sum = sum + next_term
        print(next_term, end =" ")

    return sum

sum = sum_fibonacci(terms)
print(f"\nSum of fibonacci terms upto {terms}: {sum}")