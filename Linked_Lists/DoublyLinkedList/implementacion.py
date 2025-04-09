class DoublyNode[T]:
    """
    DoublyNode class

    Node class for DoublyLinkedList

    Attributes:
    data: T
        The data to be stored in the node
    next: DoublyNode[T] | None
        The next node in the linked list
    prev: DoublyNode[T] | None
        The previous node in the linked list
    """

    def __init__(self, data: T):
        self.data: T = data
        self.next: DoublyNode[T] | None = None
        self.prev: DoublyNode[T] | None = None


class DoublyLinkedList[T]:
    """
    DoublyLinkedList class

    Attributes:
    head: DoublyNode[T] | None
        The head of the linked list
    """

    def __init__(self):
        self.head: DoublyNode[T] | None = None

    def is_empty(self) -> bool:
        """
        Check if the linked list is empty
        Returns: bool - True if the linked list is empty, False otherwise
        """
        return self.head is None

    def insert(self, data: T) -> None:
        """
        Insert a new node at the beginning of the linked list

        :param data: T - The data to be stored in the new node
        """
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_at(self, new_data: T, goal: Any, key: Callable[[Any], Any] = _identity) -> None:
        """
        Insert a new node after a node with a specific key

        :param new_data: T - The data to be stored in the new node
        :param goal: Any - The key to search for
        :param key: Callable[[Any], Any] - The function to extract the key from the data. Default is the identity
            function

        :raises ValueError: If the linked list is empty
        :raises KeyError: If the key is not found
        """
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)
        current = self.head
        while current:
            if key(current.data) == goal:
                new_node = DoublyNode(new_data)
                new_node.next = current.next
                new_node.prev = current
                current.next = new_node
                return
            current = current.next
        raise KeyError(_KEY_NOT_FOUND)

    def append(self, data: T) -> None:
        """
        Append a new node at the end of the linked list

        :param data: T - The data to be stored in the new node
        """
        new_node = DoublyNode(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def reverse(self) -> None:
        """
        Reverse the linked list in place

        """
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)
        previous = None
        current = self.head
        while current:
            next_node = current.next
            current.next = previous
            current.prev = next_node
            previous = current
            current = next_node
        self.head = previous

    def find(self, goal: Any, key: Callable[[T], Any] = _identity) -> DoublyNode[T] | None:
        """
        Find the first node with a specific key

        :param goal: Any - The key to search for
        :param key: Callable[[T], Any] - The function to extract the key from the data. Default is the identity function

        :return: DoublyNode[T] | None - The node with the key or None if not found
        """
        current = self.head
        while current:
            if key(current.data) == goal:
                return current
            current = current.next
        return None

    def delete(self, goal: Any, key: Callable[[T], Any] = _identity) -> None:
        """
        Delete the first node with a specific key

        :param goal: Any - The key to search for
        :param key: Callable[[T], Any] - The function to extract the key from the data. Default is the identity function

        :raises ValueError: If the linked list is empty
        :raises KeyError: If the key is not found
        """
        if self.is_empty():
            raise ValueError(_LIST_IS_EMPTY)
        if key(self.head.data) == goal:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if key(current.next.data) == goal:
                current.next = current.next.next
                return
            current = current.next
        raise KeyError(_KEY_NOT_FOUND)

    def clear(self) -> None:
        """
        Clear the linked list
        """
        self.head = None

    def __contains__(self, item: Any) -> bool:
        """
        Check if the linked list contains a specific item

        :param item: Any - The item to search for

        :return: bool - True if the item is found, False otherwise
        """
        return self.find(item) is not None

    def __len__(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self) -> str:
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return " <-> ".join(map(str, result))

    def __repr__(self) -> str:
        return f"DoublyLinkedList([{', '.join(repr(data) for data in self)}])"