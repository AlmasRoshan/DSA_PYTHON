# Trees and Heaps: Quick Revision Sheet

---

## 1. Introduction to Trees

### Why Do We Need Trees?
* Linear structures (`Array`, `LinkedList`, `Stack`, `Queue`) store data sequentially.
* Linear search takes $O(N)$ time, while ordered arrays take $O(N)$ for insertions and deletions.
* Trees represent **hierarchical data** (file systems, HTML DOM, organizational charts) and allow efficient searching, insertion, and deletion ($O(\log N)$ when balanced).

### Core Components of a Tree
* **Node:** Contains data and pointers/references to other nodes.
* **Root:** The topmost node with no parent.
* **Edge:** The connection/link between two nodes.
* **Parent & Child:** A node directly above another is its parent; the node below is the child.
* **Leaf Node:** A node with no children (degree 0).
* **Subtree:** Any node and all of its descendants.
* **Depth:** Number of edges from the root to that node.
* **Height:** Number of edges on the longest path from that node down to a leaf.

---

## 2. Binary Tree (BT)

A tree where every node has **at most 2 children** (referred to as `left` and `right`).

### Types of Binary Trees

| Type | Definition |
| :--- | :--- |
| **Full Binary Tree** | Every node has either **0 or 2 children** (never just 1 child). |
| **Complete Binary Tree** | All levels are completely filled except possibly the last, and the last level is filled from **left to right** without gaps. |
| **Perfect Binary Tree** | All internal nodes have 2 children, and all leaf nodes are at the **same level**. |
| **Skewed Binary Tree** | Every node has only one child (either all left-skewed or all right-skewed). Effectively behaves like a linked list ($O(N)$ operations). |

### Tree Representation in Python

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example: Root with two children
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

---

## 3. Tree Traversals

### Depth-First Search (DFS) Traversals

1. **In-order (Left $\rightarrow$ Root $\rightarrow$ Right):**
   * For a BST, this visits nodes in **sorted ascending order**.
2. **Pre-order (Root $\rightarrow$ Left $\rightarrow$ Right):**
   * Useful for copying or serializing a tree.
3. **Post-order (Left $\rightarrow$ Right $\rightarrow$ Root):**
   * Useful for deleting a tree or bottom-up calculations (e.g., node heights).

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Breadth-First Search (BFS) / Level-Order Traversal

Visits nodes level by level from top to bottom, left to right. Uses a **queue**.

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
        
    return result
```

---

## 4. Binary Search Tree (BST)

### The BST Property
For every node $X$:
* All values in the **left subtree** are strictly **smaller** than $X$.
* All values in the **right subtree** are strictly **greater** than $X$.

> **Relationship:** Every BST is a Binary Tree, but **not** every Binary Tree is a BST.

### Core Operations

```python
class BST:
    # 1. Search
    def search(self, root, target):
        if not root or root.val == target:
            return root
        if target < root.val:
            return self.search(root.left, target)
        return self.search(root.right, target)

    # 2. Insert
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    # 3. Delete
    def delete_node(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            # Case 1 & 2: 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: 2 children -> replace with in-order successor (min in right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.delete_node(root.right, curr.val)
            
        return root
```

---

## 5. Heaps (Priority Queues)

A Heap is a specialized **Complete Binary Tree** stored typically in an array/list.

### Types of Heaps
* **Min-Heap:** The root is the minimum element. For every node: `Parent <= Children`.
* **Max-Heap:** The root is the maximum element. For every node: `Parent >= Children`.

### Array Representation Formula (0-indexed)
For an element at index $i$:
* **Parent:** `(i - 1) // 2`
* **Left Child:** `2 * i + 1`
* **Right Child:** `2 * i + 2`

### Python `heapq` and the Negative Values Trick
Python's standard `heapq` module is a **Min-Heap** by default.

To simulate a **Max-Heap**, multiply all values by `-1` when inserting, and multiply by `-1` again when retrieving:

```python
import heapq

nums = [10, 4, 15, 20, 2]

# Min-Heap (default)
min_heap = nums.copy()
heapq.heapify(min_heap)
print(heapq.heappop(min_heap))  # 2 (smallest element)

# Max-Heap trick using negative numbers
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

# The "smallest" negative is the largest original value
largest = -heapq.heappop(max_heap)
print(largest)  # 20 (largest element)
```

---

## 6. Comparison: Binary Tree vs BST vs Heap

| Feature | Binary Tree (BT) | Binary Search Tree (BST) | Binary Heap |
| :--- | :--- | :--- | :--- |
| **Ordering Rule** | None | Left < Root < Right | Parent $\le$ Children (Min) or Parent $\ge$ Children (Max) |
| **Shape Requirement** | None | None (can become skewed) | Must be a **Complete Binary Tree** |
| **Duplicate Keys** | Allowed | Typically not allowed or placed in right | Allowed |
| **Typical Implementation** | Node pointers | Node pointers | Dynamic array / list |
| **Primary Use Case** | Hierarchy representation | Fast search, sorted iteration | Priority queues, finding min/max |

---

## 7. Time Complexities

| Data Structure / Operation | Search | Insertion | Deletion | Find Min / Max |
| :--- | :--- | :--- | :--- | :--- |
| **Binary Tree** | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **BST (Average)** | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ |
| **BST (Worst / Skewed)** | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **Binary Heap** | $O(N)$ | $O(\log N)$ | $O(\log N)$ | $O(1)$ (peek root) |

> **Heap Construction Note:** Building a heap from an unsorted list (`heapify`) takes **$O(N)$** time, not $O(N \log N)$.
# Trees and Heaps: Quick Revision Sheet

---

## 1. Introduction to Trees

### Why Do We Need Trees?
* Linear structures (`Array`, `LinkedList`, `Stack`, `Queue`) store data sequentially.
* Linear search takes $O(N)$ time, while ordered arrays take $O(N)$ for insertions and deletions.
* Trees represent **hierarchical data** (file systems, HTML DOM, organizational charts) and allow efficient searching, insertion, and deletion ($O(\log N)$ when balanced).

### Core Components of a Tree
* **Node:** Contains data and pointers/references to other nodes.
* **Root:** The topmost node with no parent.
* **Edge:** The connection/link between two nodes.
* **Parent & Child:** A node directly above another is its parent; the node below is the child.
* **Leaf Node:** A node with no children (degree 0).
* **Subtree:** Any node and all of its descendants.
* **Depth:** Number of edges from the root to that node.
* **Height:** Number of edges on the longest path from that node down to a leaf.

---

## 2. Binary Tree (BT)

A tree where every node has **at most 2 children** (referred to as `left` and `right`).

### Types of Binary Trees

| Type | Definition |
| :--- | :--- |
| **Full Binary Tree** | Every node has either **0 or 2 children** (never just 1 child). |
| **Complete Binary Tree** | All levels are completely filled except possibly the last, and the last level is filled from **left to right** without gaps. |
| **Perfect Binary Tree** | All internal nodes have 2 children, and all leaf nodes are at the **same level**. |
| **Skewed Binary Tree** | Every node has only one child (either all left-skewed or all right-skewed). Effectively behaves like a linked list ($O(N)$ operations). |

### Tree Representation in Python

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Example: Root with two children
#       1
#      / \
#     2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
```

---

## 3. Tree Traversals

### Depth-First Search (DFS) Traversals

1. **In-order (Left $\rightarrow$ Root $\rightarrow$ Right):**
   * For a BST, this visits nodes in **sorted ascending order**.
2. **Pre-order (Root $\rightarrow$ Left $\rightarrow$ Right):**
   * Useful for copying or serializing a tree.
3. **Post-order (Left $\rightarrow$ Right $\rightarrow$ Root):**
   * Useful for deleting a tree or bottom-up calculations (e.g., node heights).

```python
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root):
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def postorder(root):
    if not root:
        return []
    return postorder(root.left) + postorder(root.right) + [root.val]
```

### Breadth-First Search (BFS) / Level-Order Traversal

Visits nodes level by level from top to bottom, left to right. Uses a **queue**.

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(current_level)
        
    return result
```

---

## 4. Binary Search Tree (BST)

### The BST Property
For every node $X$:
* All values in the **left subtree** are strictly **smaller** than $X$.
* All values in the **right subtree** are strictly **greater** than $X$.

> **Relationship:** Every BST is a Binary Tree, but **not** every Binary Tree is a BST.

### Core Operations

```python
class BST:
    # 1. Search
    def search(self, root, target):
        if not root or root.val == target:
            return root
        if target < root.val:
            return self.search(root.left, target)
        return self.search(root.right, target)

    # 2. Insert
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left, val)
        elif val > root.val:
            root.right = self.insert(root.right, val)
        return root

    # 3. Delete
    def delete_node(self, root, key):
        if not root:
            return None
        
        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            # Case 1 & 2: 0 or 1 child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: 2 children -> replace with in-order successor (min in right subtree)
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.delete_node(root.right, curr.val)
            
        return root
```

---

## 5. Heaps (Priority Queues)

A Heap is a specialized **Complete Binary Tree** stored typically in an array/list.

### Types of Heaps
* **Min-Heap:** The root is the minimum element. For every node: `Parent <= Children`.
* **Max-Heap:** The root is the maximum element. For every node: `Parent >= Children`.

### Array Representation Formula (0-indexed)
For an element at index $i$:
* **Parent:** `(i - 1) // 2`
* **Left Child:** `2 * i + 1`
* **Right Child:** `2 * i + 2`

### Python `heapq` and the Negative Values Trick
Python's standard `heapq` module is a **Min-Heap** by default.

To simulate a **Max-Heap**, multiply all values by `-1` when inserting, and multiply by `-1` again when retrieving:

```python
import heapq

nums = [10, 4, 15, 20, 2]

# Min-Heap (default)
min_heap = nums.copy()
heapq.heapify(min_heap)
print(heapq.heappop(min_heap))  # 2 (smallest element)

# Max-Heap trick using negative numbers
max_heap = [-x for x in nums]
heapq.heapify(max_heap)

# The "smallest" negative is the largest original value
largest = -heapq.heappop(max_heap)
print(largest)  # 20 (largest element)
```

---

## 6. Comparison: Binary Tree vs BST vs Heap

| Feature | Binary Tree (BT) | Binary Search Tree (BST) | Binary Heap |
| :--- | :--- | :--- | :--- |
| **Ordering Rule** | None | Left < Root < Right | Parent $\le$ Children (Min) or Parent $\ge$ Children (Max) |
| **Shape Requirement** | None | None (can become skewed) | Must be a **Complete Binary Tree** |
| **Duplicate Keys** | Allowed | Typically not allowed or placed in right | Allowed |
| **Typical Implementation** | Node pointers | Node pointers | Dynamic array / list |
| **Primary Use Case** | Hierarchy representation | Fast search, sorted iteration | Priority queues, finding min/max |

---

## 7. Time Complexities

| Data Structure / Operation | Search | Insertion | Deletion | Find Min / Max |
| :--- | :--- | :--- | :--- | :--- |
| **Binary Tree** | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **BST (Average)** | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ |
| **BST (Worst / Skewed)** | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **Binary Heap** | $O(N)$ | $O(\log N)$ | $O(\log N)$ | $O(1)$ (peek root) |

> **Heap Construction Note:** Building a heap from an unsorted list (`heapify`) takes **$O(N)$** time, not $O(N \log N)$.