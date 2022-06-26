'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        accessed = [[False] * n for _ in range(m)]

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
        m, n = len(grid), len(grid[0])
        curr_queue = [(i, j)]
        offset = itertools.product([-1, 0, 1], [-1, 0, 1])
        offset = [(di, dj) for di, dj in offset if di * dj == 0 and di != dj]
        while curr_queue:
            i, j = curr_queue.pop()
            accessed[i][j] = True
            move = [(i + di, j + dj) for di, dj in offset]
            move = [(x, y) for x, y in move if 0 <= x < m and 0 <= y < n]
            move = [(x, y) for x, y in move if not accessed[x][y] and grid[x][y] == '1']
            for x, y in move:
                curr_queue.append((x, y))


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
