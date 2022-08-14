'''
459. Repeated Substring Pattern
https://leetcode.com/problems/repeated-substring-pattern/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        jump_cache = [0] * len(s)

        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[j] != s[i]:
                j = jump_cache[j - 1]
            if s[j] == s[i]:
                j += 1
            jump_cache[i] = j
        if jump_cache[-1] == 0:
            return False
        return not len(s) % (len(s) - jump_cache[-1])

    def _repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        t = t[1:-1]
        return t != t.replace(s, '')

    def __repeatedSubstringPattern(self, s: str) -> bool:
        m = 2
        while m <= len(s):
            if len(s) % m != 0:
                m += 1
                continue
            if not s.replace(s[:len(s) // m], ''):
                return True
            m += 1
        return False