'''
583. Delete Operation for Two Strings
https://leetcode.com/problems/delete-operation-for-two-strings/
'''
import collections
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [
            [0] * (n + 1) for _ in range(m + 1)
        ]

        for x in range(m + 1):
            dp[x][0] = x
        for y in range(n + 1):
            dp[0][y] = y

        word1 = ' ' + word1
        word2 = ' ' + word2
        for x, y in itertools.product(range(1, m + 1), range(1, n + 1)):
            if word1[x] == word2[y]:
                dp[x][y] = dp[x - 1][y - 1]
            else:
                dp[x][y] = 1 + min(dp[x - 1][y], dp[x][y - 1])
        return dp[-1][-1]

    def _minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        word1 = f' {word1}'
        word2 = f' {word2}'

        for i in range(m + 1):
            dp[i][0] = i

        for i in range(n + 1):
            dp[0][i] = i

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 2, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

        return dp[-1][-1]
