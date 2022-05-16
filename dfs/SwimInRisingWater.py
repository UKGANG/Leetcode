'''
778. Swim in Rising Water
https://leetcode.com/problems/swim-in-rising-water/
'''
import heapq
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set([(0, 0)])
        q = [(grid[0][0], 0, 0)]
        res = grid[0][0]
        while q:
            level, x, y = heapq.heappop(q)
            res = max(res, level)
            if x == y == n - 1:
                return res
            move = [(dx, dy) for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1])]
            move = [(dx, dy) for dx, dy in move if dx * dy == 0 and dx != dy]
            move = [(x + dx, y + dy) for dx, dy in move]
            move = [(i, j) for i, j in move if 0 <= i < n and 0 <= j < n]
            move = [(i, j) for i, j in move if (i, j) not in visited]
            for i, j in move:
                heapq.heappush(q, (grid[i][j], i, j))
                visited.add((i, j))


assert_value(3, Solution().swimInWater, grid=[
    [0, 2],
    [1, 3]
])
assert_value(16, Solution().swimInWater, grid=[
    [0, 1, 2, 3, 4],
    [24, 23, 22, 21, 5],
    [12, 13, 14, 15, 16],
    [11, 17, 18, 19, 20],
    [10, 9, 8, 7, 6]
])
