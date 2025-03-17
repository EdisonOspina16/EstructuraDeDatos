from queue import Queue

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