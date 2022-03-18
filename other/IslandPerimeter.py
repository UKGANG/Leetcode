'''
463. Island Perimeter
https://leetcode.com/problems/island-perimeter/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                res += 4
                if i - 1 > -1 and grid[i - 1][j] == 1:
                    res -= 1
                if j - 1 > -1 and grid[i][j - 1] == 1:
                    res -= 1
                if i + 1 < len(grid) and grid[i + 1][j] == 1:
                    res -= 1
                if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
                    res -= 1
        return res


assert_value(10, Solution().islandPerimeter, grid=[
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
])
assert_value(16, Solution().islandPerimeter, grid=[
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
])
assert_value(4, Solution().islandPerimeter, grid=[
    [1]
])
assert_value(4, Solution().islandPerimeter, grid=[
    [1, 0]
])
