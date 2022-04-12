'''
329. Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
'''
from typing import List, Optional

from test_tool import assert_value


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        def dfs(i, j):
            if dp[i][j]:
                return dp[i][j]
            for x, y in [
                (i - 1, j),
                (i, j - 1),
                (i + 1, j),
                (i, j + 1),
            ]:
                if 0 <= x < m and 0 <= y < n:
                    if matrix[i][j] > matrix[x][y]:
                        dp[i][j] = max(dp[i][j], dfs(x, y))
            dp[i][j] += 1
            return dp[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


assert_value(4, Solution().longestIncreasingPath, matrix=[[9, 9, 4], [6, 6, 8], [2, 1, 1]])
assert_value(4, Solution().longestIncreasingPath, matrix=[[3, 4, 5], [3, 2, 6], [2, 2, 1]])
assert_value(1, Solution().longestIncreasingPath, matrix=[[1]])
