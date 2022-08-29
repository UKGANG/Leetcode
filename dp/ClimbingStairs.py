'''
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
'''
import functools
from typing import List, Final, Optional

from test_tool import assert_value


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [None] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]

    def _climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        dp_1, dp_2 = 2, 1
        for i in range(3, n + 1):
            res = dp_1 + dp_2
            dp_1, dp_2 = res, dp_1
        return res
