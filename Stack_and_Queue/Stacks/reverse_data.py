from stack import Stack

def reverse_data(file_pad: str):
    stack = Stack()
    with open(file_pad, "r", encoding = "utf8") as file:
        for line in file:
            stack.push(line.strip())
    while not stack.is_empty():
        print(stack.pop())

print(reverse_data("data.txt"))