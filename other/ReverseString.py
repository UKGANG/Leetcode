'''
344. Reverse String
https://leetcode.com/problems/reverse-string/
'''
import re
from typing import List

from test_tool import assert_value


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        m = (len(s) >> 1)
        for i in range(m):
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]

        return s


assert_value(["o", "l", "l", "e", "h"], Solution().reverseString, s=["h", "e", "l", "l", "o"])
assert_value(["h", "a", "n", "n", "a", "H"], Solution().reverseString, s=["H", "a", "n", "n", "a", "h"])
