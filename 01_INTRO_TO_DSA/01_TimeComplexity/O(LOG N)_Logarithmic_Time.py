# O(LOG N) - Logarithmic Time
# HALVE AND SEARCH
# Each step cuts the problem size in half. Even if the input size is huge, the number of steps will be small.

def binary_search(sorted_list, target):

    # low = 0
    # high = len(sorted_list) - 1      # 8 - 1 = 7
    low, high = 0, len(sorted_list) - 1
    while low <=high:
        mid = (low + high) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            low = mid + 1
        else: 
            high = mid - 1
    return -1  # Target not found
print(binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5))  # Output: 4