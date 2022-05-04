'''
317. Shortest Distance from All Buildings
https://leetcode.com/problems/shortest-distance-from-all-buildings/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            m, n = len(grid), len(grid[0])
            visited = set()
            stack = [(x, y)]
            dist = 0
            n_connected_buildings = 0
            while stack:
                stack_new = []
                for x, y in stack:
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    cnt_connections[x][y] += 1
                    dists[x][y] += dist
                    if grid[x][y] == 1:
                        n_connected_buildings += 1

                    if grid[x][y] == 1 and dist > 0:
                        continue
                    for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
                        if dx == dy:
                            continue
                        if dx != 0 and dy != 0:
                            continue
                        _x, _y = x + dx, y + dy
                        if not (0 <= _x < m and 0 <= _y < n):
                            continue
                        if (_x, _y) in visited:
                            continue
                        if grid[_x][_y] == 2:
                            continue
                        stack_new.append((_x, _y))
                stack = stack_new
                dist += 1
            return n_connected_buildings

        m, n = len(grid), len(grid[0])
        dists = [[0] * n for _ in range(m)]
        cnt_connections = [[0] * n for _ in range(m)]
        n_buildings = sum(1 for x, y in itertools.product(range(m), range(n)) if grid[x][y] == 1)

        for x, y in itertools.product(range(m), range(n)):
            if grid[x][y] == 1:
                n_connection = bfs(x, y)
                if n_connection != n_buildings:
                    return -1

        res = float('inf')
        for x, y in itertools.product(range(m), range(n)):
            if cnt_connections[x][y] == n_buildings and grid[x][y] != 1:
                res = min(res, dists[x][y])
        if res == float('inf'):
            res = -1
        return res


assert_value(7, Solution().shortestDistance, grid=[[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
assert_value(1, Solution().shortestDistance, grid=[[1, 0]])
assert_value(-1, Solution().shortestDistance, grid=[[1]])
assert_value(-1, Solution().shortestDistance, grid=[[1, 1], [0, 1]])
