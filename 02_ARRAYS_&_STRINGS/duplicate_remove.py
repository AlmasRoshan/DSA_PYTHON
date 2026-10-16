#Write second_largest(nums) returning the second-largest num. Test on [45, 88, 90, 12, 90]

def second_largest(nums):
    # to remove duplicate
        # list() to convert dict into list
        # dict.fromkeys() removes duplicate without changing order of the list
    dup = list(dict.fromkeys(nums)) # [45, 88, 12, 90]
    dup.sort() # arranging in asce
    return dup[-2] # index num -2
print(second_largest([45, 88, 90, 12, 90])) # 88

"""
def second_largest(nums):
    # remove duplicate using set(),this change list order
    dup = sorted(set(nums))
    return dup[-2]
print(second_largest([45, 88, 90, 12, 90])) # 88

"""

# var.sort() --> LIST
# sorted(var) --> STR
