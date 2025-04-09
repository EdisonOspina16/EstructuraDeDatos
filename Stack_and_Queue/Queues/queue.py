class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return "Cola Vacia"

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        if len(self.queue) == 0:
            return self.is_empty()
        return self.queue.pop()

    def frist(self):
        if len(self.queue) == 0:
            return self.is_empty()
        return self.queue[-1]

    def __str__(self):
        return str(self.queue)

    def __len__(self):
        if len(self.queue) == 0:
            return self.is_empty()
