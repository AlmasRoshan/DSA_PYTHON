# SEARCHING IN LINKED LIST

def search(self, value):
    current = self.head
    position = 0
    while current is not None:
        if current.data == value:
            return position  # Return the position of the node if the value is found
        current = current.next
        position += 1
    return -1  # Return -1 if the value is not found in the linked list