'''
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
'''
import functools
from typing import List, Final, Optional

from test_tool import assert_value


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        dp = cost
        dp.append(0)
        for i in range(2, len(dp)):
            dp[i] += min(dp[i - 1], dp[i - 2])
        return dp[-1]

    def _minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)
        dp = [0] * (len(cost) + 1)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(cost) + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + (cost[i] if i < len(cost) else 0)
        return dp[-1]
