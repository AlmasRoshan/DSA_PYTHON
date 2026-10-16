# INSERTING NODES IN A LINKED LIST

#INSERT AT THE BEGINNING OF A LINKED LIST
def insert_at_beginning(self, data):
    new_node = Node(data)   # Create a new node with the given data
    new_node.next = self.head   # Set the next pointer of the new node to the current head of the linked list
    self.head = new_node # Set the head of the linked list to the new node, making it the first node in the list


#INSERT AT THE END OF A LINKED LIST
def insert_at_end(self, data):
    new_node = Node(data)   # Create a new node with the given data
    # If the linked list is empty, set the head to the new node
    if self.head is None:
        self.head = new_node
        return
    # Traverse the linked list to find the last node
    current = self.head
    while current.next is not None:
        current = current.next
    current.next = new_node   # Set the next pointer of the last node to the new node, making it the last node in the list


#INSERT AT A SPECIFIC POSITION IN A LINKED LIST
def insert_at_position(self, data, position):
    # If the position is 0, insert the new node at the beginning of the linked list
    if position == 0:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return
    # If the position is greater than 0, traverse the linked list to find the node at the specified position
    current = self.head
    for _ in range(position - 1):
        if current is None:
            print("position is out of range")
            return
        current = current.next
    if current is None:
        print("position is out of range")
        return
    # Create a new node with the given data and insert it at the specified position
    new_node = Node(data)
    new_node.next = current.next
    current.next = new_node