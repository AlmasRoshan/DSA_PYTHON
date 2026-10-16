# SPACE COMPLEXITY

# O(1) space complexity
def built_in_max(marks):
    return max(marks)
print(built_in_max([67, 45, 89, 23, 91, 56, 78, 34])) # Output: 91

# O(N) space complexity
def double_marks(marks):
    doubled = []
    for mark in marks:
        doubled.append(mark * 2)
    return doubled
print(double_marks([10, 20 ,30])) # Output: [20, 40, 60]

# O(N) Recursive space complexity
def cout_down(n):
    if n <= 0:
        return
    print(n)
    cout_down(n - 1)
print(cout_down(5)) # Output: 5 4 3 2 1

# O(N^2) space complexity
def create_matrix(n):
    matrix = []
    # range(n) generates a sequence of numbers from 0 to (n-1) = (3 - 1 = 2),
    # which is used to create the rows of the matrix
    #range(start, stop, step) generates a sequence of numbers from start to stop (exclusive) with a step size of step.
    for i in range(n):   
        row = []
        for j in range(n):
            row.append(i * j)
        matrix.append(row)
    return matrix
print(create_matrix(3)) # Output: [[0, 0, 0], [0, 1, 2], [0, 2, 4]]