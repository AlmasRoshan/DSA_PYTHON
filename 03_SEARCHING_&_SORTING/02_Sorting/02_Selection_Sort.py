# SELECTION SORT
# sorts a list by finding the smallest element in the unsorted part of the list and swapping it with the first unsorted element

def selection_sort(items):
    n = len(items)
    # outer loop for number of passes
    for i in range(n - 1):
        min_index = i
        # inner loop for finding the index of the smallest element in the unsorted part of the list
        for j in range(i + 1,n):
            if items[j] < items[min_index]:
                min_index = j
                items[i], items[min_index] = items[min_index], items[i]
    return items
print(selection_sort([3, 20, 14, 5])) # Output: [3, 5, 14, 20]