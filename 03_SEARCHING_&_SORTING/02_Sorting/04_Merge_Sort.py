# MERGE SORT
# sorts a list by using the divideand conquer method, 
# dividing the list into halves, sorting each half, and then merging the sorted halves back together

def merge_sort(items):
    # base case for recursion
    if len(items) <= 1:
        return items
    mid = len(items) // 2
    left = merge_sort(items[ :mid])
    right = merge_sort(items[mid :])
    return merge(left, right)

def merge(left, right):
    results = []
    # pointers for left and right lists
    i = j = 0
    # merging the two sorted lists
    while i < len(left) and j < len(right):
        # comparing the elements of the two lists and adding the smaller one to the results list
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1

    # adding the remaining elements of the left and right lists to the results list
    results.extend(left[i:])
    results.extend(right[j:])
    return results
print(merge_sort([3, 20, 14, 5])) # Output: [3, 5, 14, 20]