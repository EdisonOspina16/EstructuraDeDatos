from Linked_Lists import DoublyLinkedList


class ExtendedDoublyLinkedList[T](DoublyLinkedList):
    def remove_all(self, value: T):
        current = self.head

        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                    if current.next:
                        current.next.prev = current.prev

            current = current.next

def exercise_3():
    dll = ExtendedDoublyLinkedList[int]()
    for value in [10, 20, 30, 20, 40, 50, 20]:
        dll.append(value)

    print(f"original List: {dll}")
    dll.remove_all(20)
    print(f"original List: {dll}")


if __name__ == "__main__":
    exercise_3()