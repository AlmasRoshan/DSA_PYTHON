#LINEAR SEARCH
# it works on sorted and unsorted list too

marks = [78, 92, 55, 88, 67, 95, 81, 45, 73, 90]

def linear_search(items, target):
    for index, item in enumerate(items):
        # check if the current item is equal to the target
        if item == target:
            # return the index of the target if found
            return index
    return -1   # not found
print(linear_search(marks, 88)) # Output: 3