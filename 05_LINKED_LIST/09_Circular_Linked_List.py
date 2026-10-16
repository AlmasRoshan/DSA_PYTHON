# CIRCULAR LINKED LIST
# single node consists of 2 parts: data and next
# In a circular linked list, the last node points back to the first node, forming a circle.

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = CNode(data)
        # If the list is empty, make the new node the head and point it to itself
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # Point the new node to itself
            return
        # If the list is not empty, traverse to the last node and insert the new node
        current = self.head
        while current.next is not self.head:  # Traverse until we reach the last node
            current = current.next
        current.next = new_node
        new_node.next = self.head  # Point the new node to the head

    def display(self, rounds=1):
        # check if the list is empty
        if self.head is None:
            print("Circular linked list is empty.")
            return
        current = self.head
        arr = []
        count = 0
        total = 0
        temp = self.head
        while True:
            total += 1
            temp = temp.next
            if temp == self.head:
                break
        while count < total * rounds:
            arr.append(str(current.data))
            current = current.next
            count += 1
        print(" -> ".join(arr) + " -> (back to head)")

cll = CircularLinkedList()
for val in [10, 20, 30, 40, 50]:
    cll.insert_at_end(val)
cll.display(rounds=3)  # Display the circular linked list for 3 rounds