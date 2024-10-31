'''
50. Pow(x, n)
https://leetcode.com/problems/powx-n/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 0 if not x else 1
        p = n
        if p < 0:
            p *= -1
        res = self._pow(x, p)
        if n < 0:
            res = 1/res
        return res

    def _pow(self, x: float, n: int) -> float:
        if not n:
            return x
        res = self.myPow(x * x, n >> 1)

        if n & 1:
            res *= x
        return res
    def myPow_v1(self, x: float, n: int) -> float:
        if not n:
            return 0 if not x else 1
        res = 1.

        m = n if n > 0 else -n

        while m > 0:
            if m & 1:
                res *= x
            x *= x
            m = m >> 1

        if n < 0:
            res = 1 / res
        return res

assert_value(0, Solution().myPow, x=0, n=0)
assert_value(1, Solution().myPow, x=0.1, n=0)
assert_value(1024.00000, Solution().myPow, x=2.00000, n=10)
assert_value(9.26100, Solution().myPow, x=2.10000, n=3)
# assert_value(0.25000, Solution().myPow, x=2.00000, n=-2)