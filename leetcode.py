# This will be my Python playground. I can only learn syntax by doing.

from typing import Optional
from packages.dsa.LinkedList import ListNode
from collections import deque


class Solution:

    # 1. Two Sum
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        m = {}
        for i in range(len(nums)):
            mi = target - nums[i]
            if mi in m:
                return [i, m[mi]]
            m[nums[i]] = i

        return []

    # 20. Valid Parentheses
    def isValid(self, s: str) -> bool:
        stack = []
        m = {"(": ")", "[": "]", "{": "}"}

        for i in range(len(s)):
            c = s[i]
            if c in ["(", "[", "{"]:
                stack.append(c)
            elif c in [")", "]", "}"]:
                if len(stack) > 0:
                    top = stack[-1]
                    if m[top] == c:
                        stack.pop()
                    else:
                        return False
                else:
                    return False

        return len(stack) == 0

    # 225. Implement Stack using Queues
    # TODO: we can do better than this... feels like cheating
    class MyStack:

        def __init__(self):
            self.queue = deque()

        def push(self, x: int) -> None:
            self.queue.append(x)

            n = self.size()
            if n > 1:
                for _ in range(n - 1):
                    self.queue.append(self.queue.popleft())

        def pop(self) -> int:
            return self.queue.popleft()

        def top(self) -> int:
            return self.queue[0]

        def size(self) -> int:
            return len(self.queue)

        def empty(self) -> bool:
            return self.size() < 1

    # 232. Implement Queue using Stacks
    class MyQueue:

        def __init__(self):
            self.stack = []
            self.s = []

        def push(self, x: int) -> None:
            while self.stack:
                self.s.append(self.stack.pop())

            self.s.append(x)
            while self.s:
                self.stack.append(self.s.pop())

        def pop(self) -> int:
            return self.stack.pop()

        def peek(self) -> int:
            return self.stack[-1]

        def empty(self) -> bool:
            return not self.stack

    '''TODO: 705. Design HashSet
    class MyHashSet:

        def __init__(self):
            pass

        def add(self, key: int) -> None:
            pass

        def remove(self, key: int) -> None:
            pass

        def contains(self, key: int) -> bool:
            pass

    TODO: 706. Design HashMap
    class MyHashMap:

        def __init__(self):
            pass

        def put(self, key: int, value: int) -> None:
            pass

        def get(self, key: int) -> int:
            pass

        def remove(self, key: int) -> None:
            pass'''


if __name__ == "__main__":
    print("Why did you wake me up?")
