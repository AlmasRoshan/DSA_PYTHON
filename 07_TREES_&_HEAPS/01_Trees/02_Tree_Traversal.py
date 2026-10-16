# TREE TRAVERSAL
from collections import deque   # for BFS

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# INORDER TRAVERSAL (L -> ROOT -> R), (SORTED ORDER)
# visits left subtree then parent to right child and then root and moves to right part same from botto to top
def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)
inorder(root)
print() # to start in new line (\n)

# PREORDER TRAVERSAL (ROOT -> L -> R)
# visit root first, then it's left subtree and then right subtree
def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)
preorder(root)
print() # to start in new line (\n)

# POSTORDER TRAVERSAL(L -> R -> ROOT)
# vist from down to top, left to right
def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")
postorder(root)
print()

# LEVEL ORDER TRAVERSAL(BFS: BREADTH-FIRST SEARCH)
# visits tree level-by-level
def level_order(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
level_order(root)