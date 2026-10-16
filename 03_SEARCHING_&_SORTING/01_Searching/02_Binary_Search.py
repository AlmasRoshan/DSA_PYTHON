# BINARY SEARCH
# it only works on sorted list

list = [1, 2, 3, 4, 5, 6, 7, 8]

def binary_serach(sorted_list, target):
    # low = 0
    # high = len(sorted_list) - 1
    low, high = 0, len(sorted_list) - 1
    while low <= high:
        # mid formula
        mid = (low + high) //2
        # comparing the target with mid val
        # if not mid then check the val is less than target or greater than target
        if sorted_list[mid] == target:
            return mid
        # val less than target
        elif sorted_list[mid] < target:
            low = mid +1
        # val greater than target
        else:
            high = mid - 1
    return -1  # Target not found
print(binary_serach(list, 5))  # Output: 4