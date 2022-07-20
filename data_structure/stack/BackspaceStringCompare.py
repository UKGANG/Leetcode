'''
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = []
        for c in s:
            if c == '#':
                if i:
                    i.pop()
            else:
                i.append(c)
        j = []
        for c in t:
            if c == '#':
                if j:
                    j.pop()
            else:
                j.append(c)

        return ''.join(i) == ''.join(j)


assert_value(True, Solution().backspaceCompare, s="ab#c", t="ad#c")
assert_value(True, Solution().backspaceCompare, s="ab##", t="c#d#")
assert_value(False, Solution().backspaceCompare, s="a#c", t="b")
