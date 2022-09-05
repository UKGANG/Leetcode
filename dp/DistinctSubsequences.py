'''
115. Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)

        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        s = f' {s}'
        t = f' {t}'

        for i in range(n + 1):
            dp[0][i] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if t[i] == s[j]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
        return dp[-1][-1]
