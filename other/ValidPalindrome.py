'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def _isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalpha() or c.isnumeric())
        m_revierse = len(s) >> 1
        return s[:len(s) >> 1] == s[~0:~m_revierse: -1]

    def __isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalpha() or c.isnumeric())
        m_revierse = (len(s) >> 1) - 1
        if len(s) & 1:
            m_revierse += 1
        return s[:len(s) >> 1] == s[-1:m_revierse: -1]

    def ___isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalpha() or c.isnumeric())
        for i in range(len(s) >> 1):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


assert_value(True, Solution().isPalindrome, s="A man, a plan, a canal: Panama")
assert_value(False, Solution().isPalindrome, s="race a car")
assert_value(True, Solution().isPalindrome, s=" ")
assert_value(True, Solution().isPalindrome, s="aa")
