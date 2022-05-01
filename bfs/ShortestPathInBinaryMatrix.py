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
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        q = [(0, 0, 1)]
        for x, y, depth in q:
            if x + 1 == n and y + 1 == n:
                return depth
            points = itertools.product([-1, 0, 1], [-1, 0, 1])
            points = [(x + a, y + b) for a, b in points]
            points = [(max(0, a), max(0, b)) for a, b in points]
            points = [(min(n - 1, a), min(n - 1, b)) for a, b in points]
            points = [(a, b) for a, b in points if a != x or b != y]
            points = set(points)
            for a, b in points:
                if grid[a][b] == 1:
                    continue
                grid[a][b] = 1
                q.append((a, b, depth + 1))

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
