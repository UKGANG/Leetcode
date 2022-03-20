'''
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return self.check(s, l + 1, r) or self.check(s, l, r - 1)
        return True

    def check(self, s: str, l: int, r: int):
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
