'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        accessed = []
        for i in range(len(grid)):
            accessed.append([False for i in range(len(grid[0]))])

        for i in range(len(accessed)):
            for j in range(len(accessed[0])):
                if accessed[i][j]:
                    continue
                if '0' == grid[i][j]:
                    accessed[i][j] = True
                    continue
                cnt += 1
                self.dfs(grid, accessed, i, j)
        return cnt

    def dfs(self, grid, accessed, i, j):
        accessed[i][j] = True
        if i + 1 < len(grid) and not accessed[i + 1][j] and '1' == grid[i + 1][j]:
            self.dfs(grid, accessed, i + 1, j)
        if j + 1 < len(grid[0]) and not accessed[i][j + 1] and '1' == grid[i][j + 1]:
            self.dfs(grid, accessed, i, j + 1)
        if i > 0 and not accessed[i - 1][j] and '1' == grid[i - 1][j]:
            self.dfs(grid, accessed, i - 1, j)
        if j > 0 and not accessed[i][j - 1] and '1' == grid[i][j - 1]:
            self.dfs(grid, accessed, i, j - 1)


assert_value(1, Solution().numIslands, grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])

assert_value(3, Solution().numIslands, grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])

assert_value(1, Solution().numIslands, grid=[
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]
])

assert_value(3, Solution().numIslands, grid=[
    ["1", "0", "1", "1", "0", "1", "1"]
])
