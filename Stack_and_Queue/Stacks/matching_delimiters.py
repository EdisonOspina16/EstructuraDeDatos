from stack import Stack

def is_matched(expr: str):
    left = "({["
    right = ")}]"
    stack = Stack()
    for c in expr:
        if c in left:
            stack.push(c)
        elif c in right:
            if stack.is_empty():
                return False
            if right.index(c) != left.index(stack.pop()):
                return False
    if stack.is_empty():
        return True

print(is_matched("{[((5+x)-(y+z))]}"))
