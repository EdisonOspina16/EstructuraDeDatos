from Linked_Lists import SinglyLinkedList
from typing import TypeVar, Generic

T = TypeVar("T")


class ExtendedLinkedList(SinglyLinkedList, Generic[T]):
    def has_cycle(self) -> bool:
        if self.is_empty():
            return False
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def insert_sorted(self, data: T) -> None:
        new_node = Node(data)

        if not self.head or self.head.data >= data:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        new_node.prev = current
        current.next = new_node


    def remove_cycle(self):
        if self.is_empty():
            return

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

            if slow != fast:
                return

            slow = self.head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None


def exercise_5():
    ll = ExtendedLinkedList[int]()
    for value in [1,2,3,4,5]:
        ll.append(value)

    print(ll)

    print(f"List has cicle: {ll.has_cycle()}")
    ll.head.next.next.next.next.next = ll.head.next.next

    print(f"List has cicle: {ll.has_cycle()}")

    ll.remove_cycle()
    print(f"List has cicle: {ll.has_cycle()}")


def exercise_1():
    dll = ExtendedLinkedList[int]()
    for value in [40, 10, 30, 20, 50]:
        dll.insert_sorted(value)
    print(dll)

exercise_1()

