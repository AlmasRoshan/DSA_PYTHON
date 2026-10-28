from collections import deque

class Node:
    def __init__(self, data=0):
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

def level_order(root):
    if root is None:
        return
    result = []
    queue = deque([root])
    while queue:
        level_size = len(queue)
        curr_level = []
        for _ in range(level_size):
            node = queue.popleft()
            curr_level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(curr_level)
    return result
print(level_order(root))