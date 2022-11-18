"""
1706. Where Will the Ball Fall
https://leetcode.com/problems/where-will-the-ball-fall/
"""
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        def bfs(x, y):
            if grid[x][y] == 1 and (y + 1 == n or grid[x][y + 1] == -1) \
                    or grid[x][y] == -1 and (y == 0 or grid[x][y - 1] == 1):
                return -1
            if x == m - 1:
                return y + 1 if grid[x][y] == 1 else y - 1
            if grid[x][y] == 1:
                return bfs(x + 1, y + 1)
            else:
                return bfs(x + 1, y - 1)

        m, n = len(grid), len(grid[0])
        res = [-1] * n

        for i in range(n):
            res[i] = bfs(0, i)

        return res
