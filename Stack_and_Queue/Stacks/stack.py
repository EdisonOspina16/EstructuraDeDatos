class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack) == 0

    def is_empty(self):
        if len(self.stack) == 0:
            return "Pila Vacia"

    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if len(self.stack) == 0:
            return self.is_empty()
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return self.is_empty()
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)

