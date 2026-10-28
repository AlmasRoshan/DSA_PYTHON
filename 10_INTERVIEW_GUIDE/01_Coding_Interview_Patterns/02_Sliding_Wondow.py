# SLIDING WINDOW

def max_add(nums, k):
    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - 1] # add new, drop old
        best = max(best, window)
    return best
print(max_add([2, 1, 5, 3, 2, 1], 3))