from typing import Optional, TypeVar
T = TypeVar("T")


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: T, next=None):
        self.val = val
        self.next = next


# Definition for singly-linked list.
class DoubleListNode:
    def __init__(self, val: T, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList():

    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def insertAt(self, index: int, item: T) -> None:
        if index == 0:
            self.prepend(item)
            return
        elif index == self.length:
            self.append(item)
            return
        elif index > self.length or index < 0:
            raise IndexError("tried removing out of bounds", index, self.length)

        i = 0
        curr, prev = self.head, None
        while i < index:
            if curr.next == None:
                return
            prev = curr
            curr = curr.next
            i += 1

        curr.next = prev.next
        prev.next = curr
        self.length += 1

    def remove(self, item: T) -> Optional[T]:
        if self.length == 0:
            return None

        # check head
        if self.head.val == item:
            v = self.head.val
            self.head = self.head.next
            self.length -= 1
            return v
        elif self.length == 1:
            return None

        # scan list for value
        curr, prev = self.head, None
        while curr and curr.val != item:
            prev = curr
            curr = curr.next

        if curr == None:
            return None
        else:
            v = curr.val
            prev.next = curr.next
            self.length -= 1
            curr = None
            return v

    def removeAt(self, index: int) -> Optional[T]:
        if self.length == 0:
            return None

        if index >= self.length or index < 0:
            raise IndexError("tried removing out of bounds: {}/{}", index, self.length)
        i = 0
        curr, prev = self.head, None
        while i < index:
            if curr.next == None:
                return None
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next
        self.length -= 1
        return curr.val

    def append(self, item: T) -> None:
        n = ListNode(item)

        if self.head is None:
            self.head = n
            self.length += 1
            return

        curr = self.head
        while curr.next:
            curr = curr.next

        curr.next = n
        self.length += 1

    def prepend(self, item: T) -> None:
        n = ListNode(item)

        if self.head is None:
            self.head = n
            self.length += 1
            return

        n.next = self.head
        self.head = n
        self.length += 1

    def get(self, index: int) -> Optional[T]:
        if index >= self.length:
            return None

        i, curr = 0, self.head
        while curr.next and i < index:
            curr = curr.next
            i += 1

        return None if i < index else curr.val
