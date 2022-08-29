'''
62. Unique Paths
https://leetcode.com/problems/unique-paths/
'''
import functools
from typing import List, Final, Optional

from test_tool import assert_value


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        n, k = m + n - 2, min(m, n) - 1
        k = min(k, n - k)
        numerator = denominator = 1
        for i in range(0, k):
            numerator *= n
            denominator *= k
            n -= 1
            k -= 1

        return int(numerator / denominator)

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
