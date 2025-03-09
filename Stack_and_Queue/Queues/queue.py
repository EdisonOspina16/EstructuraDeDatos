class EmptyStack(Exception):
    pass


class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, e):
        self.queue.append(e)

    def dequeue(self):
        if len(self.queue) == 0:
            raise EmptyStack
        return self.queue.pop()

    def frist(self):
        if len(self.queue) == 0:
            raise EmptyStack
        return self.queue[-1]

    def __str__(self):
        return str(self.queue)

    def __len__(self):
        if len(self.queue) == 0:
            return "Cola Vacia"


def is_simmetric(numbers: list[int]) -> bool:
    queue = Queue()
    for numbers in numbers:
        queue.enqueue(numbers)

        i = -1
        while len(queue) > 1:
            if queue.dequeue() != numbers[i]:
                return False
            i -= 1

        return True

numbers = [1, 2, 3, 4, 3 ,2, 1]
print(is_simmetric(numbers))
