# BUBBLE SORT
# sorts a list one by one by comparing adjacent elements and swapping them if they are in the wrong order

def bubble_sort(items):
    n = len(items) 
    # outer loop for number of passes
    for i in range(n - 1):
        swapped = False
        # inner loop for comparing adjacent elements
        for j in range(n - 1 - i):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
                # if no two elements were swapped in the inner loop, then the list is already sorted
        if not swapped:
            break
    return items
print(bubble_sort([3, 20, 14, 5]))