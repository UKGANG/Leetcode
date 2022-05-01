'''
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        res = 0
        stack = 0
        for c in s:
            if c not in '()':
                continue
            if c == '(':
                stack += 1
            else:
                if stack:
                    stack -= 1
                else:
                    res += 1
        return res + stack


assert_value(1, Solution().minAddToMakeValid, s="())")
assert_value(3, Solution().minAddToMakeValid, s="(((")
