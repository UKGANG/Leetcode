'''
1293. Shortest Path in a Grid with Obstacles Elimination
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution(object):
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        q = collections.deque()
        visited = set()
        m, n = len(grid), len(grid[0])
        x, y, k, step = 0, 0, k - grid[0][0], 0
        q.append((x, y, k, step))

        while q:
            x, y, k, step = q.popleft()
            if x == m - 1 and y == n - 1:
                return step
            direction = [
                (x + 1, y),
                (x, y + 1),
                (x - 1, y),
                (x, y - 1),
            ]
            for _x, _y in direction:
                if not (0 <= _x < m and 0 <= _y < n):
                    continue
                _k, _step = k - grid[_x][_y], step + 1
                if _k < 0:
                    continue
                if (_x, _y, _k) in visited:
                    continue
                q.append((_x, _y, _k, _step))
                visited.add((_x, _y, _k))

        return -1


assert_value(6, Solution().shortestPath, grid=[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], k=1)
assert_value(-1, Solution().shortestPath, grid=[[0, 1, 1], [1, 1, 1], [1, 0, 0]], k=1)
assert_value(14, Solution().shortestPath,
             grid=[
                 [0, 0],
                 [1, 0],
                 [1, 0],
                 [1, 0],
                 [1, 0],
                 [1, 0],
                 [0, 0],
                 [0, 1],
                 [0, 1],
                 [0, 1],
                 [0, 0],
                 [1, 0],
                 [1, 0],
                 [0, 0]
             ]
             , k=4)
