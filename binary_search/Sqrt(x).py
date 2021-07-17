'''
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x
        l, r = 1, x
        while l < r:
            m = (l + r) >> 1
            if m * m <= x:
                l = m + 1
            else:
                r = m
        return l - 1


assert_value(1, Solution().mySqrt, x=1)
assert_value(2, Solution().mySqrt, x=4)
assert_value(2, Solution().mySqrt, x=8)
