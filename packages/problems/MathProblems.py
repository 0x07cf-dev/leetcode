class Solution:

    # 67. Add Binary
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        k = 0
        res = []

        while i >= 0 or j >= 0 or k:
            if i >= 0:
                k += int(a[i])
                i -= 1

            if j >= 0:
                k += int(b[j])
                j -= 1

            res.insert(0, k % 2)
            k //= 2

        return "".join(res)

    # 69. sqrt(x)
    def mySqrt(self, x: int) -> int:
        if x < 0:
            raise NotImplementedError

        def squared(n):
            return n * n

        # binary search from 0 to x
        lo, hi = 0, x
        while squared((lo + hi) // 2) != x:
            mid = (lo + hi) // 2

            if squared(mid) > x:
                hi = mid - 1
            else:
                lo = mid + 1

            if lo > hi:
                return hi

        return (lo + hi) // 2
