'''
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)

    def _dp_isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        s = f' {s}'
        t = f' {t}'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i][j - 1]

        return max(sum(dp, [])) == m
