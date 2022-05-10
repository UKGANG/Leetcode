'''
1091. Shortest Path in Binary Matrix
https://leetcode.com/problems/shortest-path-in-binary-matrix/
'''
import collections
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        m, n = len(grid), len(grid[0])
        visited = set()
        curr_level = set([(0, 0)])
        res = 0
        while curr_level:
            res += 1
            next_level = set()
            for x, y in curr_level:
                if (x, y) == (m - 1, n - 1):
                    return res
                move = itertools.product([-1, 0, 1], [-1, 0, 1])
                move = [(dx, dy) for dx, dy in move if dx != 0 or dy != 0]
                move = [(x + dx, y + dy) for dx, dy in move]
                move = [(i, j) for i, j in move if 0 <= i < m and 0 <= j < n]
                move = [(i, j) for i, j in move if grid[i][j] == 0]
                move = [(i, j) for i, j in move if (i, j) not in visited]
                [visited.add((i, j)) for i, j in move]
                [next_level.add((i, j)) for i, j in move]
            curr_level = next_level

        return -1


assert_value(2, Solution().shortestPathBinaryMatrix, grid=[[0, 1], [1, 0]])
assert_value(4, Solution().shortestPathBinaryMatrix, grid=[[0, 0, 0], [1, 1, 0], [1, 1, 0]])
assert_value(-1, Solution().shortestPathBinaryMatrix, grid=[[1, 0, 0], [1, 1, 0], [1, 1, 0]])
assert_value(14, Solution().shortestPathBinaryMatrix, grid=[
    [0, 1, 1, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0],
    [1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0]
])
