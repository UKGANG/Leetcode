'''
205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        cache_s = {}
        cache_t = {}

        for i in range(len(s)):
            si = s[i]
            ti = t[i]

            if si not in cache_s and ti not in cache_t:
                cache_s[si] = i
                cache_t[ti] = i
                continue

            if si not in cache_s or ti not in cache_t:
                return False

            if cache_s[si] != cache_t[ti]:
                return False

        return True


assert_value(True, Solution().isIsomorphic, s="egg", t="add")
assert_value(False, Solution().isIsomorphic, s="foo", t="bar")
assert_value(True, Solution().isIsomorphic, s="paper", t="title")
