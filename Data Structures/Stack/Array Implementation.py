class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop() if self.stack else "Stack is empty"

    def peek(self):
        return self.stack[-1] if self.stack else "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
stack.push(10)
stack.push(20)
print("Popped:", stack.pop())  # Output: 20
print("Top:", stack.peek())  # Output: 10
