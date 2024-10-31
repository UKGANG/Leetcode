'''
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l_idx, r_idx = 0, len(s) - 1
        return self._check(s, 1, l_idx, r_idx)

    def _check(self, s: str, available_removal: int, l_idx: int, r_idx: int) -> bool:
        if l_idx >= r_idx:
            return True
        if s[l_idx] == s[r_idx]:
            return self._check(s, available_removal, l_idx + 1, r_idx - 1)
        if not available_removal:
            return False
        return (
                self._check(s, available_removal - 1, l_idx + 1, r_idx)
                or self._check(s, available_removal - 1, l_idx, r_idx - 1)
        )

    def _validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.check_v1(s, l + 1, r) or self.check_v1(s, l, r - 1)
        return True

    def check_v1(self, s: str, l: int, r: int):
        if l == r:
            return True
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


assert_value(True, Solution().validPalindrome, s="aba")
assert_value(True, Solution().validPalindrome, s="abca")
assert_value(False, Solution().validPalindrome, s="abc")
assert_value(True, Solution().validPalindrome, s="deeee")
assert_value(True, Solution().validPalindrome, s="cbbcc")
assert_value(True, Solution().validPalindrome, s="acbca")
