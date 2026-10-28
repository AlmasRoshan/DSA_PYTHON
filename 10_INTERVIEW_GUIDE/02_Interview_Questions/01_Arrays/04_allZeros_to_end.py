# Move all zeros to the end

def all_zeros_to_end(nums):
    position = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[position], nums[i] = nums[i], nums[position]
            position += 1
    return nums
print(all_zeros_to_end([1, 0 ,2 , 0, 3, 4]))