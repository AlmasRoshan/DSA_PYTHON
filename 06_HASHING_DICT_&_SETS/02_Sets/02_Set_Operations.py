# SET OPERATIONS - MODIFYING SETS, COMBINING SETS

# MODIFYING SETS
s = {1, 2, 3, 4, 5}

# ADDING ELEMENTS TO A SET
s.add(6)  # Add a single element to the set
s.add(2)  # Adding a duplicate element has no effect
print(sorted(s))  # Output: [1, 2, 3, 4, 5, 6]

# REMOVING ELEMENTS FROM A SET
s.remove(3)  # Remove an element from the set; raises KeyError if the element is not found
s.remove(10)  # Raises KeyError since 10 is not in the set
s.discard(4)  # Remove an element from the set; does not raise an error if the element is not found
s.discard(10)  # Does not raise an error since 10 is not in the set
print(sorted(s))  # Output: [1, 2, 5, 6]

# pop() - Remove and return an arbitrary element from the set; raises KeyError if the set is empty
removed_element = s.pop()
print("Removed element:", removed_element) # Output: Removed element: 1 (the removed element may vary)
print(sorted(s))  # Output: [2, 5, 6] (the removed element may vary)

# copy() and clear() - Create a shallow copy of the set and remove all elements from the set
copy = s.copy()  # Create a shallow copy of the set
s.clear()  # Remove all elements from the set
print(s)  # Output: set() (the original set is now empty)
print(copy)  # Output: {2, 5, 6} (the copy remains unchanged)

#-----------------------------------------------------------------------------------------------------------

# COMBINING SETS

num_1 = {1, 2, 3, 4, 5}
num_2 = {4, 5, 6, 7, 8}

# UNION - Combine two sets to create a new set containing all unique elements from both sets
print(num_1 | num_2)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

union_set = num_1.union(num_2)  # Create a new set containing all unique elements from both sets
print(union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# INTERSECTION - Create a new set containing only the elements that are present in both sets
print(num_1 & num_2)  # Output: {4, 5}

intersection_set = num_1.intersection(num_2)  # Create a new set containing only the elements that are present in both sets
print(intersection_set)  # Output: {4, 5}

# DIFFERENCE 
# Create a new set containing the elements that are present in the first set but not in the second set
print(num_1 - num_2)  # Output: {1, 2, 3}
difference_set = num_1.difference(num_2)  # Create a new set containing the elements that are present in the first set but not in the second set
print(difference_set)  # Output: {1, 2, 3}

# Create a new set containing the elements that are present in the second set but not in the first set
print(num_2 - num_1)  # Output: {8, 6, 7}
difference_set_2 = num_2.difference(num_1)  # Create a new set containing the elements that are present in the second set but not in the first set
print(difference_set_2)  # Output: {8, 6, 7}

# SYMMETRIC DIFFERENCE - Create a new set which contains not repetitive elements from both sets (elements that are in either of the sets but not in both)
print(num_1 ^ num_2)  # Output: {1, 2, 3, 6, 7, 8}

symmetric_difference_set = num_1.symmetric_difference(num_2)  # Create a new set which contains not repetitive elements from both sets (elements that are in either of the sets but not in both)
print(symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}
