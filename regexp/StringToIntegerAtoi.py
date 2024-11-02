'''
8. String to Integer (atoi)
https://leetcode.com/problems/string-to-integer-atoi/
'''
import re
from typing import List

from test_tool import assert_value


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        idx = 0
        while idx < len(s) and s[idx] == '0':
            idx += 1
        s = s[idx:]
        idx = 0
        while idx < len(s) and s[idx].isdigit():
            idx += 1
        s = s[: idx]
        if not s:
            return 0
        if sign > 0:
            return min(int(s), (1 << 31) - 1)
        else:
            return -min(int(s), (1 << 31))

    def myAtoi_v0(self, s: str) -> int:
        matcher = re.match(r'^\s*([+|-]?\d+)', s)
        digit = 0
        if matcher:
            digit = int(matcher.group())
        if digit < 0:
            return max(-(1 << 31), digit)
        return min((1 << 31) - 1, digit)


assert_value(42, Solution().myAtoi, s="42")
assert_value(-42, Solution().myAtoi, s="   -42")
assert_value(4193, Solution().myAtoi, s="4193 with words")
assert_value(0, Solution().myAtoi, s="words and 987")
assert_value(-2147483648, Solution().myAtoi, s="-91283472332")
assert_value(0, Solution().myAtoi, s=".1")
