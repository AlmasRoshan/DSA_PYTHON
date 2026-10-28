def prefix_sum(nums):
    prefix = [0]
    running_total = 0
    for num in nums:
        running_total += num
        prefix.append(running_total)
    return prefix

def range_sum(prefix, i ,j):
    return prefix[j + 1] - prefix[i]

nums = [2, 4, 1, 3, 5]
prefix = prefix_sum(nums)
result = range_sum(prefix, 1, 3)
print("sum of index 1 to 3:", result)