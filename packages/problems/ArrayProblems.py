class Solution:

    # 26. Remove Duplicates from Sorted Array
    def removeDuplicates(self, nums: list[int]) -> int:
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

    # 27. Remove Element In Place
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        I = []

        for i in range(n):
            if nums[i] == val:
                I.insert(0, i)

        for i in I:
            nums.pop(i)

        return len(nums)

    # 35. Search Insert Position (O(log n))
    def searchInsert(self, nums: list[int], target: int) -> int:
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

    # 66. Plus One
    def plusOne(self, digits: list[int]) -> list[int]:
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
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
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
