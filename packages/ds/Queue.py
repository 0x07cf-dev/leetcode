from typing import Optional, TypeVar, Generic
from packages.ds.LinkedList import ListNode
T = TypeVar("T")


class Queue(Generic[T]):
    def __init__(self) -> None:
        self.head = self.tail = None
        self.length = 0

    def enqueue(self, item: T) -> None:
        n = ListNode(item)

        self.length += 1
        if not self.tail:
            self.head = self.tail = n
            return

        self.tail.next = n
        self.tail = n

    def deque(self) -> Optional[T]:
        if not self.head:
            return None

        self.length -= 1

        v = self.head
        self.head = self.head.next

        # free mem
        v.next = None
        return v.val

    def peek(self) -> Optional[T]:
        return self.head.val if self.head else None
