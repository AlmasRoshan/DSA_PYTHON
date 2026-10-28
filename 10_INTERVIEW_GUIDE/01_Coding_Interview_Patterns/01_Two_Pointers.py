# TWO POINTERS

def two_pointer(sorted, target):
    left, right = 0, len(sorted) - 1
    while left < right:
        total = sorted[left] + sorted[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False
print(two_pointer([1, 3, 5, 7, 9], 12))