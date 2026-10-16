# QUICK SORT
# sorts a list by using the divide and conquer method,
# selecting a pivot element, pivot = last element of the list, 
# and partitioning the list into two sublists, one with elements less than the pivot and the other with elements greater than the pivot, and then recursively sorting the sublists

def quick_sort(items):
    # base case for recursion
    if len(items) <= 1:
        return items

    # last element of the list is chosen as the pivot
    pivot = items[-1]
    # less than or equal to pivot and greater than pivot lists are created using list comprehensions
    smaller = [x for x in items[:-1] if x <= pivot]
    larger = [x for x in items[:-1] if x > pivot]
    return quick_sort(smaller) + [pivot] + quick_sort(larger)
print(quick_sort([3, 20, 14, 5])) # Output: [3, 5, 14, 20]