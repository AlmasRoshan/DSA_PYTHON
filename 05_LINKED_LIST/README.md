# Linked Lists

---

## 1. Introduction & Node Structure

A Linked List is a linear data structure where elements are not stored in contiguous memory locations. Instead, elements are linked using object references (pointers).

* **Head**: Reference pointing to the first node.
* **Node**: Individual element containing data and link(s).
* **Tail**: The final node, which references `None` in linear lists.

### Python Node Definition

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

---

## 2. Structure Types & Diagrams

### Singly Linked List (SLL)
Unidirectional chain where each node references the next node.

```text
[Head] -> [Data | Next] -> [Data | Next] -> [Data | None]
```

### Doubly Linked List (DLL)
Bidirectional chain containing forward and backward pointers.

```text
None <- [Prev | Data | Next] <-> [Prev | Data | Next] -> None
```

### Circular Linked List (CLL)
End node loops back to link directly with the head node.

```text
[Head] -> [Data | Next] -> [Data | Next]
   ^                            |
   +----------------------------+
```

---

## 3. Basic Traversal & Search

### Traversal

```python
curr = head
while curr:
    print(curr.data)
    curr = curr.next
```

### Linear Search

```python
def search(head, target):
    curr = head
    while curr:
        if curr.data == target:
            return True
        curr = curr.next
    return False
```

---

## 4. Insertion Techniques

### At Beginning

```python
new_node = Node(val)
new_node.next = head
head = new_node
```

### At End

```python
new_node = Node(val)
if not head:
    head = new_node
else:
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
```

### By Position

```python
# Insert at index pos (assuming pos > 0 and within bounds)
curr = head
for _ in range(pos - 1):
    curr = curr.next
new_node = Node(val)
new_node.next = curr.next
curr.next = new_node
```

---

## 5. Deletion Techniques

### From Beginning

```python
if head:
    head = head.next
```

### From End

```python
if not head or not head.next:
    head = None
else:
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
```

### By Position

```python
# Delete at index pos
curr = head
for _ in range(pos - 1):
    curr = curr.next
curr.next = curr.next.next
```

### By Value

```python
if head and head.data == val:
    head = head.next
else:
    curr = head
    while curr.next and curr.next.data != val:
        curr = curr.next
    if curr.next:
        curr.next = curr.next.next
```

---

## 6. Reversing a Singly Linked List

Iterative three-pointer approach:

```python
prev = None
curr = head

while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

head = prev
```

---

## 7. Comparative Overview

| Operation | Array / Dynamic List | Singly Linked List |
| :--- | :--- | :--- |
| **Prepend (Insert at 0)** | O(n) | O(1) |
| **Append (Insert at End)** | O(1) amortized | O(n) (O(1) with tail ref) |
| **Lookup by Index** | O(1) | O(n) |
| **Search by Value** | O(n) | O(n) |
| **Memory Layout** | Contiguous blocks | Scattered references |