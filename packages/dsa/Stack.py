from typing import Optional, TypeVar, Generic
from packages.dsa.LinkedList import ListNode
T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def push(self, item: T) -> None:
        n = ListNode(item)

        self.length += 1
        if not self.head:
            self.head = n
            return

        n.next = self.head
        self.head = n

    def pop(self) -> Optional[T]:
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
