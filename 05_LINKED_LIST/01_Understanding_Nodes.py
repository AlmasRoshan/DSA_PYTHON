# Every node in a linked list has two parts: data and a pointer to the next node. 
# The last node points to None, indicating the end of the list.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
a = Node(10)
b = Node(20)
c = Node(30)
a.next = b
b.next = c
print(a.data) # 10
print(a.next.data) # 20
print(a.next.next.data) # 30