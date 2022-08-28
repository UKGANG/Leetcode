'''
509. Fibonacci Number
https://leetcode.com/problems/fibonacci-number/
'''
import functools
from typing import List, Final, Optional

from test_tool import assert_value


class Solution:
    def fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def _fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        n_2, n_1 = 0, 1
        res = 0
        for i in range(2, n + 1):
            res = n_2 + n_1
            n_2, n_1 = n_1, res
        return res

    @functools.lru_cache()
    def __fib(self, n: int) -> int:
        if n in [0, 1]:
            return n
        return self.__fib(n - 1) + self.__fib(n - 2)
