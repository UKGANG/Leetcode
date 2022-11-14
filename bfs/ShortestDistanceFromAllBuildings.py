'''
317. Shortest Distance from All Buildings
https://leetcode.com/problems/shortest-distance-from-all-buildings/
'''
import collections
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            nonlocal m, n
            visited = set()
            connected_building_cnt = 0
            queue = collections.deque([(x, y)])

            dist_cnt = -1
            while queue:
                dist_cnt += 1
                size = len(queue)
                for _ in range(size):
                    x, y = queue.popleft()
                    if (x, y) in visited:
                        continue
                    visited.add((x, y))
                    if grid[x][y] == 2:
                        continue
                    connected_building_cnt_matrix[x][y] += 1
                    dist_matrix[x][y] += dist_cnt
                    if grid[x][y] == 1:
                        connected_building_cnt += 1
                    if grid[x][y] == 1 and dist_cnt > 0:
                        continue
                    for dx, dy in offset:
                        _x, _y = x + dx, y + dy
                        if not 0 <= _x < m or not 0 <= _y < n:
                            continue
                        queue.append((_x, _y))
            return connected_building_cnt

        m, n = len(grid), len(grid[0])
        dist_matrix = [[0] * n for _ in range(m)]
        connected_building_cnt_matrix = [[0] * n for _ in range(m)]
        total_building_cnt = sum(1 for x, y in itertools.product(range(m), range(n)) if grid[x][y] == 1)

        offset = [(x, y) for x, y in itertools.product(range(-1, 2), range(-1, 2)) if x != y and x * y == 0]

        for x, y in itertools.product(range(m), range(n)):
            if grid[x][y] == 1:
                connected_building_cnt = bfs(x, y)
                if connected_building_cnt != total_building_cnt:
                    return -1

        res = float('inf')
        for x, y in itertools.product(range(m), range(n)):
            if connected_building_cnt_matrix[x][y] == total_building_cnt and grid[x][y] == 0:
                res = min(res, dist_matrix[x][y])

        return -1 if res == float('inf') else res


    def _shortestDistance(self, grid: List[List[int]]) -> int:
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
