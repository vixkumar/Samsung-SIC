class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return None if self.is_empty() else self.queue.pop(0)


queue = Queue()

queue.enqueue("A")
queue.enqueue("B")

print(queue.dequeue())  # A
print(queue)

queue.enqueue("C")

print(queue.dequeue())  # B
print(queue.dequeue())  # C
print(queue.dequeue())  # None


