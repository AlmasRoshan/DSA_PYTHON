# CREATING SETS

# Creating an empty set
empty_set = set()
print(empty_set)  # Output: set()
print(type(empty_set))  # Output: <class 'set'>

# Creating a set with initial elements
my_set = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, (1, 2), True}
names = {"Alice", "Bob", "Charlie"}
set_with_duplicates = {1, 2, 2, 3, 4, 4, 5}
print(set_with_duplicates)  # Output: {1, 2, 3, 4, 5} (duplicates are removed)
print(names == {"Charlie", "Bob"})  # Output: False (order doesn't matter in sets, but the elements must match)
print(names == {"Bob", "Alice", "Charlie"})  # Output: True (order doesn't matter in sets, but the elements must match)