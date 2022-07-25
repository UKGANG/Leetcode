'''
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, m):
            dp[i][0] += dp[i - 1][0]
            dp[i][0] += grid[i][0]
        for i in range(1, n):
            dp[0][i] += dp[0][i - 1]
            dp[0][i] += grid[0][i]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j]
                dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

    def _minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid) - 1, len(grid[0]) - 1
        res = {'res': float('inf')}

        def dfs(x, y, total, visited):
            if (x, y) == (n, m):
                res['res'] = min(res['res'], total)
                return
            visited[y][x] = True

            move = itertools.product([-1, 0, 1], [-1, 0, 1])
            move = [(dx, dy) for dx, dy in move if dx * dy == 0 and dx != dy]
            move = [(x + dx, y + dy) for dx, dy in move]
            move = [(x_new, y_new) for x_new, y_new in move if 0 <= x_new <= n and 0 <= y_new <= m]
            move = [(x_new, y_new) for x_new, y_new in move if not visited[y_new][x_new]]
            for x_new, y_new in move:
                dfs(x_new, y_new, total + grid[y_new][x_new], visited)
            visited[y][x] = False

        visited = [[False] * (n + 1) for _ in range(m + 1)]
        dfs(0, 0, grid[0][0], visited)

        return res['res']


assert_value(7, Solution().minPathSum, grid=[[1, 3, 1], [1, 5, 1], [4, 2, 1]])
assert_value(12, Solution().minPathSum, grid=[[1, 2, 3], [4, 5, 6]])
