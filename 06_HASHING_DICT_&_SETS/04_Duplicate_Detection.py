# DUPLICATE DETECTION

def dup(items):
    seen = set()
    for item in items:
        if item in seen:
            return True  # if item is repeated in the set the return True 
        else:
            seen.add(item) # add each item into the empty created set()
    return False   # if no item repeated in the set(all unique) them return False
print(dup([1,2,3,1,5])) # True
print(dup([1,2,3])) # False

#--------------------------------------------------------------------------------------------------------

# MEMBERSHIP TESTING

# List - slow on large scale O(n)
n = ["almas", "roshan"]
print("almas" in n)  # returns True if present
print("shaik" in n)  # returns False 

# Set - fast O(1) uses hash()
s = {1, 2, 3}
print(3 in s)   # True
print(7 in s)   # False