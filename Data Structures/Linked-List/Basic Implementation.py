class Node:
    """A class to represent a node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """A class to represent a singly linked list."""
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert a new node at the end of the linked list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the linked list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        """Delete a node by value."""
        temp = self.head

        # If the node to be deleted is the head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the node to be deleted
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:  # If the key is not found
            print("Element not found!")
            return

        prev.next = temp.next
        temp = None  # Free memory

    def search(self, key):
        """Search for an element in the linked list."""
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def display(self):
        """Display the linked list."""
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Example Usage
llist = LinkedList()
llist.insert_at_end(10)
llist.insert_at_end(20)
llist.insert_at_end(30)
llist.insert_at_beginning(5)
llist.display()  # Output: 5 -> 10 -> 20 -> 30 -> None

print("Searching for 20:", llist.search(20))  # Output: True
print("Searching for 100:", llist.search(100))  # Output: False

llist.delete_node(20)
llist.display()  # Output: 5 -> 10 -> 30 -> None
