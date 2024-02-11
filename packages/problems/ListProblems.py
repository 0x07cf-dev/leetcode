from typing import Optional
from packages.dsa.LinkedList import ListNode


class Solution:

    # 2. Add Two Numbers
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i, j, k = 0, 0, 0

        # find sum
        while l1 or l2:
            if l1:
                k += l1.val * (10 ** i)
                l1 = l1.next
                i += 1

            if l2:
                k += l2.val * (10 ** j)
                l2 = l2.next
                j += 1

        k = int(k)

        # convert to array
        head = h = ListNode()
        while k > 0:
            h.val = k % 10
            k //= 10

            if k > 0:
                h.next = ListNode()
                h = h.next

        return head

    # 21. Merge Two Sorted Lists
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        head = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next = list1
                dummy = list1
                list1 = list1.next
            else:
                dummy.next = list2
                dummy = list2
                list2 = list2.next

        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2

        return head.next
