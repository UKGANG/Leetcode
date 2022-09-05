'''
28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
'''
from typing import List, NoReturn

from test_tool import assert_value


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        jump_cache = [None] * len(needle)

        j = 0
        jump_cache[0] = 0
        for i in range(1, len(needle)):
            while j > 0 and needle[j] != needle[i]:
                j = jump_cache[j - 1]
            if needle[j] == needle[i]:
                j += 1
            jump_cache[i] = j

        j = 0
        for i in range(0, len(haystack)):
            while j > 0 and needle[j] != haystack[i]:
                j = jump_cache[j - 1]
            if needle[j] == haystack[i]:
                j += 1
            if j == len(needle):
                return i - j + 1
        return -1


assert_value(2, Solution().strStr, haystack="hello", needle="ll")
assert_value(-1, Solution().strStr, haystack="aaaaa", needle="bba")
