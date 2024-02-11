from typing import Optional, Tuple, TypeVar, Generic
T = TypeVar("T")


# Definition for singly-linked list.
class ListNode(Generic[T]):
    def __init__(self, val: T = 0, next: Optional["ListNode[T]"] = None):
        self.val = val
        self.next = next


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def prepend(self, item: T) -> None:
        n = ListNode(item)

        self.length += 1
        if self.head is None:
            self.head = n
            return

        n.next = self.head
        self.head = n

    def insertAt(self, index: int, item: T) -> None:
        if index > self.length or index < 0:
            raise IndexError("Insertion out of bounds.", index, self.length)
        elif index == self.length:
            self.append(item)
            return
        elif index == 0:
            self.prepend(item)
            return

        self.length += 1
        n = ListNode(item)
        curr, prev = self.__getAt(index)
        if curr and prev:
            prev.next = n
            n.next = curr

    def append(self, item: T) -> None:
        n = ListNode(item)

        self.length += 1
        if self.head is None:
            self.head = n
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = n

    def remove(self, item: T) -> Optional[T]:
        if self.length == 0:
            return None

        # Could it be head?
        if self.head and self.head.val == item:
            self.length -= 1
            v = self.head.val
            self.head = self.head.next
            return v
        # If it's not, but length is one...
        elif self.length == 1:
            return None

        # Scan list for value
        curr, prev = self.head, None
        while curr and curr.val != item:
            prev = curr
            curr = curr.next

        # Not found
        if curr is None or prev is None:
            return None
        else:
            self.length -= 1
            v = curr
            prev.next = curr.next

            # free mem
            v.next = None
            return v.val

    def removeAt(self, index: int) -> Optional[T]:
        if index >= self.length or index < 0:
            raise IndexError(f"Removal out of bounds. Index {index} is outside of length: {self.length}")

        self.length -= 1
        if self.length == 0:
            self.head = None

        curr, prev = self.__getAt(index)
        if curr and prev:
            prev.next = curr.next
            # free mem
            curr.next = None
            return curr.val

        return None

    def get(self, index: int) -> Optional[T]:
        node = self.__getAt(index)[0]
        return node.val if node else None

    def __getAt(self, index: int) -> Tuple[Optional[ListNode[T]], Optional[ListNode[T]]]:
        curr, prev = self.head, None
        for _ in range(index):
            if curr:
                prev = curr
                curr = curr.next

        return curr, prev


# Definition for doubly-linked list.
class DoubleListNode(Generic[T]):
    def __init__(self, val: T = 0, next: Optional["DoubleListNode[T]"] = None, prev: Optional["DoubleListNode[T]"] = None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList(Generic[T]):
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def prepend(self, item: T) -> None:
        n = DoubleListNode(item)

        self.length += 1
        if self.head is None:
            self.head = self.tail = n
            return

        n.next = self.head
        self.head.prev = n
        self.head = n

    def insertAt(self, index: int, item: T) -> None:
        if index > self.length or index < 0:
            raise IndexError("Insertion out of bounds.", index, self.length)
        elif index == self.length:
            self.append(item)
            return
        elif index == 0:
            self.prepend(item)
            return

        self.length += 1
        curr = self.__getAt(index)

        if curr:
            n = DoubleListNode(item)
            n.next = curr

            if curr.prev:
                n.prev = curr.prev
                curr.prev.next = n
                curr.prev = n

    def append(self, item: T) -> None:
        n = DoubleListNode(item)

        self.length += 1
        if self.tail is None:
            self.head = self.tail = n

        n.prev = self.tail
        self.tail.next = n
        self.tail = n

    def remove(self, item: T) -> Optional[T]:
        curr = self.head
        for _ in range(self.length):
            if curr and curr.val == item or not curr:
                break
            curr = curr.next

        return self.__remove_node(curr) if curr else None

    def removeAt(self, index: int) -> Optional[T]:
        node = self.__getAt(index)
        return self.__remove_node(node) if node else None

    def get(self, index: int) -> Optional[T]:
        node = self.__getAt(index)
        return node.val if node else None

    def __getAt(self, index: int) -> Optional[DoubleListNode[T]]:
        curr = self.head
        for _ in range(index):
            if curr:
                curr = curr.next

        return curr

    def __remove_node(self, node: DoubleListNode) -> Optional[T]:
        self.length -= 1

        if self.length == 0:
            self.head = self.tail = None

        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        # free mem
        node.prev = node.next = None
        return node.val
