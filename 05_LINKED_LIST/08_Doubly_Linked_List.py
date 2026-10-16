# DOUBLY LINKED LIST
# it contains 2 pointers, one pointing to the next node and the other pointing to the previous node.
# a single node consists of 3 parts: prev, data, next

class DNode:
    def __init__(self, data):
        self.prev = None  # Pointer to the previous node
        self.data = data  # Data stored in the node
        self.next = None  # Pointer to the next node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    def insert_at_end(self, data):
        new_node = DNode(data) # Create a new node with the given data
        # check if the list is empty
        if self.head is None:
            self.head = new_node # If the list is empty, set the head to the new node
            return
        # If the list is not empty, traverse to the end of the list
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current    # link the new node to the previous node

    def display_forward(self):
        current = self.head
        arr = []
        while current is not None:
            arr.append(str(current.data))   # str() method is used to convert the data to string before appending it to the list.
            current = current.next  # Move to the next node in the list
        print(" <-> ".join(arr))

    def display_backward(self):
        current = self.head
        # check if the list is empty
        if current is None:
            print("The list is empty.")
            return
        # Traverse to the end of the list
        while current.next is not None:
            current = current.next
        arr = []
        while current is not None:
            arr.append(str(current.data))   # str() method is used to convert the data to string before appending it to the list.
            current = current.prev  # Move to the previous node in the list
        print(" <-> ".join(arr))

dll = DoublyLinkedList()   # Create an instance of the DoublyLinkedList class
for value in [10, 20, 30, 40, 50]:   # Loop through a list of values
    dll.insert_at_end(value)
dll.display_forward()   # 10 <-> 20 <-> 30 <-> 40 <-> 50
dll.display_backward()  # 50 <-> 40 <-> 30 <-> 20 <-> 10