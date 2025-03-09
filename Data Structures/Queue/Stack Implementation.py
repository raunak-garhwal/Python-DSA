class QueueUsingStack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, data):
        self.s1.append(data)

    def dequeue(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop() if self.s2 else "Queue is empty"

queue_stack = QueueUsingStack()
queue_stack.enqueue(1)
queue_stack.enqueue(2)
print("Dequeued:", queue_stack.dequeue())  # Output: 1
