'''
72. Edit Distance
https://leetcode.com/problems/edit-distance/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i

        word1 = f' {word1}'
        word2 = f' {word2}'

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1],
                        dp[i - 1][j],
                        dp[i - 1][j - 1],
                    ) + 1
        return dp[-1][-1]

    def _su_version_minDistance(self, word1: str, word2: str) -> int:
        solution = []
        for i in range(len(word1) + 1):
            solution.append([0] * (len(word2) + 1))

        for i in range(len(word1) + 1):
            solution[i][0] = i

        for j in range(len(word2) + 1):
            solution[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                solution[i][j] = min(solution[i - 1][j - 1] + (1 if word1[i - 1] != word2[j - 1] else 0),
                                     solution[i][j - 1] + 1,
                                     solution[i - 1][j] + 1)
        return solution[i][j]


assert_value(3, Solution().minDistance, word1="horse", word2="ros")
assert_value(5, Solution().minDistance, word1="intention", word2="execution")
