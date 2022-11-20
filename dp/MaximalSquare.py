'''
221. Maximal Square
https://leetcode.com/problems/maximal-square/
'''
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [
            [0] * n for _ in range(m)
        ]

        res = 0
        for x in range(m):
            dp[x][0] = 1 if matrix[x][0] == '1' else 0
            res = 1 if matrix[x][0] == '1' else res

        for y in range(n):
            dp[0][y] = 1 if matrix[0][y] == '1' else 0
            res = 1 if matrix[0][y] == '1' else res

        for x in range(1, m):
            for y in range(1, n):
                if matrix[x][y] == '0':
                    continue
                dp[x][y] = min(dp[x - 1][y - 1], dp[x - 1][y], dp[x][y - 1]) + 1
                res = max(res, dp[x][y] * dp[x][y])
        return res
