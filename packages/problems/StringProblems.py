class Solution:

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
    def longestCommonPrefix(self, strs: list[str]) -> str:
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

    # 28. Find the Index of the First Occurrence in a String
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n):
            if haystack[i] == needle[0]:
                j = 0
                while i + j < n and haystack[i + j] == needle[j]:
                    j += 1
                    if j >= m:
                        return i

        return -1

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

    # 290. Word Pattern
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split s into tokens
        # iterate over pattern, construct dictionary of matches to check consistency
        words = s.split()
        if len(words) != len(pattern):
            return False

        D = {}
        for i in range(len(pattern)):
            ch = pattern[i]
            word = words[i]

            if not ch in D:
                # character is new, but value already exists = no match
                if word in D.values():
                    return False

                D[ch] = word
            else:
                # we've already met this letter, so let's check if it's consistent
                if word != D[ch]:
                    return False

        return True

    # 412. Fizz Buzz
    def fizzBuzz(self, n: int) -> list[str]:
        arr = []
        for i in range(1, n + 1):
            t = str(i)

            if i % 5 == 0:
                if i % 3 == 0:
                    t = "FizzBuzz"
                else:
                    t = "Buzz"
            elif i % 3 == 0:
                t = "Fizz"

            arr.append(t)
        return arr

    def fizzBuzzMap(self, n: int) -> list[str]:
        arr = []
        m = {3: "Fizz", 5: "Buzz"}

        for i in range(1, n + 1):
            t = ""
            for k in m:
                if i % k == 0:
                    t += m[k]

            arr.append(t if t else str(i))
        return arr
