class EmptyStackException(Exception):
    pass

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
            raise EmptyStackException
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise EmptyStackException
        return self.stack[-1]

    def __str__(self):
        return str(self.stack)



def is_matched_html(html: str):
    stack = Stack()
    j = html.find("<")
    while j !=-1:
        k = html.find(">", j+1)
        if k == -1:
            return False

        tag = html[j+1:k]
        if not tag.startswith("/"):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if tag[1:] != stack.pop():
                return False
        j = html.find("<", k+1)
    return stack.is_empty()


html = "<html><h1></h1></html>"
print(is_matched_html(html))