class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class QueueLL:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if not self.front:
            return "Queue is empty"
        temp = self.front.data
        self.front = self.front.next
        return temp

queue_ll = QueueLL()
queue_ll.enqueue(1)
queue_ll.enqueue(2)
print("Dequeued:", queue_ll.dequeue())  # Output: 1
