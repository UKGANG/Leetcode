"""
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome
"""
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        res = 0
        orphan = False
        for v in counter.values():
            res += v >> 1 << 1
            if v & 1:
                orphan = True
        if orphan:
            res += 1
        return res