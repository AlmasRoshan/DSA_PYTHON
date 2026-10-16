# BINARY TREE REPRESENTATION

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)
print(root.data)    #50
print(root.left.data)   #30
print(root.right.data)  #70