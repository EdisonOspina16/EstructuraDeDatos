class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root, key= lambda x: x):
        self.root = root
        self.key = key
        self._size: int = 0

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(self.root, data)
        self._size += 1

    def _insert(self, node: Node, data):
        if self.key(data) < self.key(node.data):
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(node.right, data)

    def delete(self, goal):
        self.root = self._delete(self.root, goal)
        # verificar que si se encontro el elemento
        self._size -= 1

    def _delete(self, node: Node, goal):
        if node is None:
            return node

        if self.key(goal) < self.key(node.data):
            node.left = node.left = self._delete(node.left, goal)
        elif self.key(goal) > self.key(node.data):
            node.right = self._delete(node.right, goal)
        else:
            if node.left is None:
                temp = node.right

            if node.right is None:
                temp = node.left

            node.data = self._min_value(node.right)
            node.right =self._delete(node.right, node.data)
        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = node.left
        return current

    def print_tree(self, node=None, prefix="", is_left=True):

        if node is None:
            node = self.root
            if node is None:
                print("Empty Tree")
                return

        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)

        print(prefix + ("└── " if is_left else "┌── ") + str(node.data))

        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

    def buscar(self):
        pass

    def altura(self):
        pass

if __name__ == "__main__":
    tree = BinarySearchTree(None)
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(2)
    tree.insert(7)
    tree.insert(12)
    tree.insert(18)
    tree.insert(20)
    tree.insert(13)
    tree.insert(14)
    tree.insert(17)
    tree.insert(19)
    tree.insert(6)
    tree.insert(8)
    tree.insert(9)
    tree.print_tree()
    tree.delete(18)
    tree.print_tree()
