# Find a pair with a given sum(two pointers)

def two_pointers(nums, target):
    nums.sort() # sort the list if it isn't 
    left, right = 0, len(nums)- 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return True
        elif total < target:
            left += 1
        else:
            right -= 1
    return False
print(two_pointers([2, 1, 6, 4, 3, 9], 6))