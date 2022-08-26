'''
455. Assign Cookies
https://leetcode.com/problems/assign-cookies/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)
        res = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                res += 1
            j += 1
        return res
