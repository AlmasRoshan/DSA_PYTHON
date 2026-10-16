# MAX HEAP
# parent is greater then the children

import heapq    

marks = [50, 30, 70, 20, 60]

# turn the list into MAX HEAP
max_heap = [-m for m in marks]
heapq.heapify(max_heap)
print(max_heap) # larger num appears first
print(-max_heap[0]) #70

# push() - push(var_name, val)
heapq.heappush(max_heap, -80)
print(max_heap) # as 80 is larger than 70, 80 appears first
print(-max_heap[0]) # 80

# pop()
remove = heapq.heappop(max_heap)
print(remove)   # pop's the larger val 80
print(max_heap) # return the larger val after pop