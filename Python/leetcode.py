# This will be my Python playground. I can only learn syntax by doing.

from typing import List, Optional
import math

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 1. Two Sum
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            mi = target - nums[i]
            if mi in hashmap:
                return [i, hashmap[mi]]
            hashmap[nums[i]] = i

    # 9. Palindrome Number
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        return str(x) == str(x)[::-1]

    # 13. Roman to Integer
    def romanToInt(self, s: str) -> int:
        RtI = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            n = RtI[s[i]]
            # If next roman digit is greater than current, subtract current
            if (i < len(s) - 1 and n < RtI[s[i + 1]]):
                total -= n
            else:
                total += n

        return total

    # 14. Longest Common Prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        shortest = strs[0]
        for i in range(1, n):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]

        while len(shortest) > 0:
            f = False
            for i in range(n):
                if shortest != strs[i][0:len(shortest)]:  # not in strs[i]:
                    l = len(shortest) - 1
                    shortest = shortest[0:l:]
                    f = True
                    break

            if not f:
                return shortest

        return ""

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

    # 21. Merge Two Sorted Lists
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        head = n = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                n.next = list1
                n = list1
                list1 = list1.next
            else:
                n.next = list2
                n = list2
                list2 = list2.next

        if list1:
            n.next = list1
        elif list2:
            n.next = list2

        return head.next

    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: List[int]) -> int:
        nlist = []

        i = 0
        while i < (len(nums)):
            j = i + 1
            nlist.append(nums[i])

            # skip indices that point to same values
            while j < len(nums) and nums[j] == nums[i]:
                j += 1

            i = j

        unique = len(nlist)
        for i in range(unique):
            nums[i] = nlist[i]
        nums = nums[:unique]

        return unique

    # 27. Remove Element
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        I = []

        for i in range(n):
            if nums[i] == val:
                I.insert(0, i)

        for i in I:
            nums.pop(i)

        return len(nums)

    # 35. Search Insert Position (O(log n))
    def searchInsert(self, nums: List[int], target: int) -> int:
        # binary search
        left, right = 0, len(nums) - 1

        while nums[(left + right) // 2] != target:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

            if left > right:
                return left

        return (left + right) // 2

    # 58. Length of Last Word
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s) - 1
        l = 0

        if last == 0:
            return 0 if s == " " else 1

        while last > 0 and s[last] == " ":
            last -= 1

        while last >= 0 and s[last] != " ":
            last -= 1
            l += 1
            if last > 0 and s[last] == " ":
                break

        return l

    # 66. Plus One
    def plusOne(self, digits: List[int]) -> List[int]:
        d = len(digits) - 1

        for i in range(d, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0

        # array of nines becomes array of zeroes, so prepend a one
        return [1] + digits

    # 88. Merge Sorted Array
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        i = m - 1
        j = n - 1
        k = m + n - 1

        while j >= 0:
            if i > -1 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

    # 108. Convert Sorted Array to Binary Search Tree
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.makeBST(nums, 0, len(nums))

    def makeBST(self, nums, i, j):
        if i >= j:
            return None
        return TreeNode(val=nums[(i + j) // 2], left=self.makeBST(nums, i, (i + j) // 2), right=self.makeBST(nums, ((i + j) // 2) + 1, j))


def main():
    sol = Solution()

    n26 = sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
    print(f"n26: {n26}")

    n27 = sol.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    print(f"n27: {n27}")

    n66 = sol.plusOne([1, 9, 9, 7, 9])
    print(f"n66: {n66}")

    nums1, m, nums2, n = [2, 0], 1, [1], 1
    sol.merge(nums1, m, nums2, n)
    nums1, m, nums2, n = [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3
    sol.merge(nums1, m, nums2, n)
    print(f"n88: {nums1}")

    n108 = sol.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(f"n108: {n108}")


if __name__ == "__main__":
    main()
