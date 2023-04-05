'''
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/
'''
import functools
from typing import List

from test_tool import assert_value


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start):
            nonlocal res, combo
            if start == len(s):
                res.append(combo[:])
                return

            for end in range(start, len(s)):
                if not self.is_palindrome(start, end, s):
                    continue
                combo.append(s[start: end + 1])
                backtrack(end + 1)
                combo.pop()

        res, combo = [], []
        backtrack(0)
        return res

    @functools.lru_cache()
    def is_palindrome(self, l, r, s):
        if l == r:
            return True
        if s[l] != s[r]:
            return False
        if l + 1 == r:
            return True
        return self.is_palindrome(l + 1, r - 1, s)


assert_value([["a", "a", "b"], ["aa", "b"]], Solution().partition, s="aab")
