# BINARY SEARCH TREE(BST)
# everything in its LEFT subtree is SMALLER, & everything in its RIGHT subtree is BIGGER
# Left < Root < Right

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def search(self, data):
        node = self.root
        while node is not None:
            if data == node.data:
                return True
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return False

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is None:
            return 
        self._inorder(node.left, result)
        result.append(node.data)
        self._inorder(node.right, result)

bst = BST()
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(val)

print("InOrder:", bst.inorder())    # prints tree in order
print("Search 70:", bst.search(70)) #True
print("Search 80:", bst.search(80)) #True