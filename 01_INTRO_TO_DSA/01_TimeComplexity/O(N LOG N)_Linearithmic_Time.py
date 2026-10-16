# O(N LOG N) - Linearithmic Time
# SORT AND SEARCH
# The time taken to execute the function grows linearly with the size of the input
# Slower than O(N) but faster than O(N^2).

def sort_marks(marks):
    return sorted(marks) # sorted() uses for sorting an algorithm called Timsort which has a time complexity of O(N log N)
print(sort_marks([88, 92, 79, 95, 85]))  # Output: [79, 85, 88, 92, 95]
