# DELETING NODES IN A LINKED LIST

# DELETE FROM THE BEGINNING OF A LINKED LIST
def delete_from_beginning(self):
    if self.head is None:  # Check if the linked list is empty
        print("Linked list is empty. Cannot delete from beginning.")
        return
    self.head = self.head.next  # Set the head of the linked list to the next node, effectively removing the first node


# DELETE FROM THE END OF A LINKED LIST
def delete_from_end(self):
    # check if the linked list is empty
    if self.head is None:
        print("Linked list is empty. Cannot delete from end.")
        return
    # only one node in the linked list
    if self.head.next is None:
        self.head = None  # Set the head to None, effectively removing the only node in the list
        return
    # more than one node in the linked list
    current = self.head
    while current.next.next is not None:  # Traverse the linked list to find the second-to-last node
        current = current.next
    current.next = None  # Set the next pointer of the second-to-last node to None, effectively removing the last node


# DELETE FROM A SPECIFIC POSITION IN A LINKED LIST
def delete_from_position(self, position):
    # check if the linked list is empty
    if self.head is None:
        print("Linked list is empty. Cannot delete from position.")
        return
    # if the position is 0, delete the first node
    if position == 0:
        self.head = self.head.next
        return
    # traverse the linked list to find the node at the specified position
    current = self.head
    for _ in range(position - 1):
        if current.next is None:
            print("Position is out of range. Cannot delete from position.")
            return
        current = current.next
    if current.next is None:
        print("Position is out of range. Cannot delete from position.")
        return
    current.next = current.next.next  # Remove the node at the specified position


# DELETE A NODE WITH A SPECIFIC VALUE IN A LINKED LIST
def delete_node_with_value(self, value):
    # check if the ll is empty
    if self.head is None:
        print("Linked list is empty. Cannot delete node with value.")
        return
    # if the value is in the first node, delete the first node
    if self.head.data ==  value:
        self.head = self.head.next  # Set the head of the linked list to the next node, effectively removing the first node
        return
    # traverse the linked list to find the node with the specified value
    current = self.head
    while current.next is not None:
        if current.next.data == value:
            current.next = current.next.next  # Remove the node with the specified value
            return
        current = current.next
    print("Node with value", value, "not found in the linked list.")    # value not found in the linked list