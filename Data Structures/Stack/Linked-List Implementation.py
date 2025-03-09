class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLL:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.top:
            return "Stack is empty"
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        return self.top.data if self.top else "Stack is empty"

stack_ll = StackLL()
stack_ll.push(10)
stack_ll.push(20)
print("Popped:", stack_ll.pop())  # Output: 20
print("Top:", stack_ll.peek())  # Output: 10
