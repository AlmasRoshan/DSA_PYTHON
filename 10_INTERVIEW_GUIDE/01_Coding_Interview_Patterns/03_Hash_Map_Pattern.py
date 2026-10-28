def two_sum(nums, target):
    seen = {}   # stores { num: index }
    for index, num in enumerate(nums):
        complement = target - num
        # check if the needed pattern is already in the dict
        if complement in seen:
            return [seen[complement], index]    # if seen the return
        else:
            seen[num] = index   # els seve the current num and its index
    return []

print(two_sum([2, 7, 11, 15], 9))
