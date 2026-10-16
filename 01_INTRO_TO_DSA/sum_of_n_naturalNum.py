# Problem: Sum of first n natural numbers
# One problem 2 approaches to solve this problem are:

# 1. Iterative approach
# run's 10 times and adds the numbers from 1 to 10
def sum_with_loop(n):
    total = 0
    for number in range(1, n + 1):
        total += number
    return total
print(sum_with_loop(10))  # Output: 55

# 2. Formula-based approach
# does in one calculation using the formula n*(n+1)/2
def sum_with_formula(n):
    return n*(n + 1) // 2
print(sum_with_formula(10)) # Output: 55