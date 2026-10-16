# O(N) - Linear Time
# GO THROUGH EACH ITEM
# The time taken to execute the function grows linearly with the size of the input.
# Double the input, double the time taken to execute the function.

def find_student(students, name):
    for index, student in enumerate(students): 
        if student == name:
            return index
    return -1  # Student not found
print(find_student(['John', 'Jane', 'Doe'], 'Jane'))  # Output: 1