'''
1937. Maximum Number of Points with Cost
https://leetcode.com/problems/maximum-number-of-points-with-cost/
'''
from typing import List, Optional, Tuple

from test_tool import assert_value


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [[0] * n for _ in range(m)]
        for j in range(n):
            dp[0][j] = points[0][j]
        for i in range(1, m):
            rolling_max = float('-inf')
            for j in range(n):
                rolling_max = max(rolling_max, dp[i - 1][j] + j)
                dp[i][j] = max(dp[i][j], points[i][j] - j + rolling_max)
            rolling_max = float('-inf')
            for j in range(n - 1, -1, -1):
                rolling_max = max(rolling_max, dp[i - 1][j] - j)
                dp[i][j] = max(dp[i][j], points[i][j] + j + rolling_max)

        return max(dp[-1])


assert_value(9, Solution().maxPoints, points=[[1, 2, 3], [1, 5, 1], [3, 1, 1]])
assert_value(11, Solution().maxPoints, points=[[1, 5], [2, 3], [4, 2]])
assert_value(10, Solution().maxPoints, points=[[10]])
