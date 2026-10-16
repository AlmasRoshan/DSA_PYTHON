# TRAVERSING A LINKED LIST

def traverse_linked_list(self):
    current = self.head
    while current is not None:  # Loop through the linked list until the current node is None (end of the list)
        print(current.data, end=" ")    # Print the data of the current node followed by a space
        current = current.next
    print()  # Print a newline after traversing the list


# 10 20 30
