class BinaryTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insertar(self, data):
        self.root = self._insertar_recursivo(self.root, data)

    def _insertar_recursivo(self, node, data):
        if node is None:
            return self.Node(data)
        if data < node.data:
            node.left = self._insertar_recursivo(node.left, data)
        else:
            node.right = self._insertar_recursivo(node.right, data)
        return node

    def _borrar_recursivo(self, node, data):
        if node is None:
            return None

        if data < node.data:
            node.left = self._borrar_recursivo(node.left, data)
        elif data > node.data:
            node.right = self._borrar_recursivo(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            sucesor = self._encontrar_min(node.right)
            node.data = sucesor.data
            node.right = self._borrar_recursivo(node.right, sucesor.data)
        return node

    def _encontrar_min(self, node):
        """Encuentra el nodo con el valor mínimo en un subárbol."""
        while node.left is not None:
            node = node.left
        return node

    def buscar(self, data):
        """Busca un nodo en el árbol y devuelve True si existe."""
        return self._buscar_recursivo(self.root, data)

    def _buscar_recursivo(self, node, data):
        if node is None:
            return False
        if data == node.data:
            return True
        if data < node.data:
            return self._buscar_recursivo(node.left, data)
        return self._buscar_recursivo(node.right, data)

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

if __name__ == "__main__":
    tree = BinaryTree()
    tree.insertar(10)
    tree.insertar(5)
    tree.insertar(15)
    tree.insertar(2)
    tree.insertar(7)
    tree.insertar(12)
    tree.insertar(18)
    tree.insertar(20)
    tree.insertar(13)
    tree.insertar(14)
    tree.insertar(17)
    tree.insertar(19)
    tree.insertar(6)
    tree.insertar(8)
    tree.insertar(9)
    tree.print_tree()