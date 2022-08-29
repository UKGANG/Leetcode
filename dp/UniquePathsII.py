'''
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1
        for i in range(n):
            if obstacleGrid[0][i]:
                break
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] += dp[i - 1][j]
                dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]

    def _uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 0 if obstacleGrid[0][0] else 1
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] if not obstacleGrid[i][0] else 0
        for i in range(1, n):
            dp[0][i] = dp[0][i - 1] if not obstacleGrid[0][i] else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    continue
                dp[i][j] += dp[i - 1][j]
                dp[i][j] += dp[i][j - 1]

        return dp[-1][-1]

    def __uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] or obstacleGrid[-1][-1]:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        obstacleGrid[0][0] = 1
        for i, j in itertools.product(range(m), range(n)):
            if i == 0 and j == 0:
                continue
            if obstacleGrid[i][j]:
                obstacleGrid[i][j] = 0
                continue
            if i > 0:
                obstacleGrid[i][j] += obstacleGrid[i - 1][j]
            if j > 0:
                obstacleGrid[i][j] += obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]


assert_value(2, Solution().uniquePathsWithObstacles, obstacleGrid=[
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
])
assert_value(1, Solution().uniquePathsWithObstacles, obstacleGrid=[
    [0, 1],
    [0, 0]
])
assert_value(7, Solution().uniquePathsWithObstacles, obstacleGrid=[
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
])
assert_value(13594824, Solution().uniquePathsWithObstacles, obstacleGrid=[
    [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
])
