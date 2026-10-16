# SINGLY LINKED LIST
# a single node consists of 2 parts: data and next(pointer to the next node)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # display the linked list
    def display(self):
        current = self.head
        arr = []
        while current is not None:
            arr.append(str(current.data))   # str() method is used to convert the data to string before appending it to the list.
            current = current.next
        arr.append("None")  # append None to indicate the end of the list
        print(" ->".join(arr))  # .join() method is used to join the elements of the list with " ->" as a separator.
