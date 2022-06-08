'''
1631. Path With Minimum Effort
https://leetcode.com/problems/path-with-minimum-effort/
'''
import heapq
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        queue = [(0, 0, 0)]
        visited = set()
        res = 0
        while queue:
            effort, x, y = heapq.heappop(queue)
            visited.add((x, y))
            res = max(res, effort)
            if (x, y) == (m - 1, n - 1):
                return res
            move = itertools.product([-1, 0, 1], [-1, 0, 1])
            move = [(dx, dy) for dx, dy in move if dx * dy == 0 and dx != dy]
            move = [(x + dx, y + dy) for dx, dy in move]
            move = [(i, j) for i, j in move if 0 <= i < m and 0 <= j < n]
            move = [(i, j) for i, j in move if (i, j) not in visited]
            for i, j in move:
                next_effort = abs(heights[x][y] - heights[i][j])
                heapq.heappush(queue, (next_effort, i, j))


assert_value(2, Solution().minimumEffortPath, heights=[
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
])
assert_value(1, Solution().minimumEffortPath, heights=[
    [1, 2, 3],
    [3, 8, 4],
    [5, 3, 5]
])
assert_value(0, Solution().minimumEffortPath, heights=[
    [1, 2, 1, 1, 1],
    [1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1],
    [1, 1, 1, 2, 1]
])
