# MINI CODING CHALLENGE

# Q: Write two python programs that finds the largest  number in a list
# marks = [67, 45, 89, 23, 91, 56, 78, 34]

# METHOD 1 - Linear Search O(N): loop throught the list , 
# keep a largeest var, update it whenever you find a bigger mark, 
# then print it
def linear_search(marks):
    largest = 0
    for mark in marks:
        if mark > largest:
            largest = mark
    return largest
print(linear_search([67, 45, 89, 23, 91, 56, 78, 34])) # Output: 91


# METHOD 2 - Built-in function O(1): use the built-in max() fun and print it
def built_in_max(marks):
    return max(marks)
print(built_in_max([67, 45, 89, 23, 91, 56, 78, 34])) # Output: 91


# ------------------------------------------------------------------------------------------------------------------------------

# Questions related to this challenge:
# 1. Which is easier to read? Which shows what's happening more clearly?
# ANS: The first method is easier to read and shows what's happening more clearly because it explicitly demonstrates the process of finding the largest number through iteration and comparison. The second method is concise but abstracts away the logic, making it less clear how the result is obtained.
 
# 2. What is method 1's time complexity and method 2's time complexity? Are both in same class?
# ANS: Method 1 has a time complexity of O(N) because it iterates through the entire list to find the largest number. Method 2 has a time complexity of O(1) because it uses the built-in max() function, which is optimized and does not require iteration over the list. Both methods are not in the same class; method 1 is linear time, while method 2 is constant time.

# 3. If both are O(N), why might a professional still  prefer max() in real code?
# ANS: A professional might prefer using max() in real code because it is a built-in function that is optimized for performance and readability. It reduces the amount of code needed, minimizes the chance of errors, and clearly communicates the intent of finding the maximum value without requiring the reader to understand the underlying logic of iteration and comparison.

