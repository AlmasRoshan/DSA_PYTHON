# REVERSING A LINKED LIST

def reverse_linked_list(self):
    prev = None
    current = self.head
    while current is not None:  # Loop through the linked list until the current node is None (end of the list)
        next_node = current.next    # Store the next node before reversing the pointer
        current.next = prev  # Reverse the next pointer of the current node to point to the previous node
        prev = current  # Move the previous pointer to the current node
        current = next_node  # Move the current pointer to the next node
    self.head = prev  # Set the head of the linked list to the last node, which is now the first node after reversal

ll = LinkedList()   # Create an instance of the LinkedList class
for val in [10, 20, 30, 40, 50]:
    ll.insert_at_end(val)
ll.reverse_linked_list()    # 50 -> 40 -> 30 -> 20 -> 10