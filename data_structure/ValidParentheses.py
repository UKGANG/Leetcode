'''
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._start = "([{"
        self._mapping = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self._start:
                stack.append(c)
                continue
            if not stack or self._mapping[stack.pop()] != c:
                return False
        return not stack


assert_value(True, Solution().isValid, s="()")
assert_value(True, Solution().isValid, s="()[]{}")
assert_value(False, Solution().isValid, s="(]")
assert_value(False, Solution().isValid, s="([)]")
