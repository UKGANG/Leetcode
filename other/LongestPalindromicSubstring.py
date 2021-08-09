'''
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        res = s[0]
        for i in range(len(s)):
            odd = self.get_logest_palindrome_by_center(s, i, i)
            even = self.get_logest_palindrome_by_center(s, i, i + 1)
            res = max(res, odd, even, key=len)
        return res

    def get_logest_palindrome_by_center(self, s, i, j):
        res = s[i]
        if j == len(s):
            j = i
        while i >= 0 and j < len(s):
            if s[i] != s[j]:
                break
            res = s[i:j + 1]
            i -= 1
            j += 1
        return res


assert_value('bab', Solution().longestPalindrome, s="babad")
assert_value('bb', Solution().longestPalindrome, s="cbbd")
assert_value('a', Solution().longestPalindrome, s="a")
assert_value('a', Solution().longestPalindrome, s="ac")
