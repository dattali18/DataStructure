class Queue:
    data: list

    def __init__(self):
        self.data = []

    def pop(self):
        return self.data.pop()

    def push(self, value):
        self.data.insert(value)

    def enqueue(self):
        return self.pop()

    def dequeue(self, value):
        self.push(value)

    def front(self):
        return self.data[0]
