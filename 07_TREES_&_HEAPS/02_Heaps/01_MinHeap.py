# MIN HEAP
# parent is smaller than children

import heapq

marks = [50, 30, 70, 20, 60]

# turn the list into MIN HEAP (smaller to larger)
heapq.heapify(marks)
print(marks)    # smallest num appear first 
print(marks[0]) # 20

# push() - insert ---> heappush(var_name, val)
heapq.heappush(marks, 10)
print(marks)    # as 10 is smaller than 20, 10 appears first
print(marks[0]) # 10

# pop() - del and return the deleated val
remove = heapq.heappop(marks)
print(remove)   # pop's the smallest val 10
print(marks)    # return the smallest val after pop