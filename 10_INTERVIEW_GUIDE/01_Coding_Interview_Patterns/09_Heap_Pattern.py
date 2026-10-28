import heapq

nums = [10, 20, 30, 40 , 50]
# heapq.nlargest/n.smallest(n, var_name)
print("largest num:", heapq.nlargest(1, nums))
print("smallest num:", heapq.nsmallest(1, nums))