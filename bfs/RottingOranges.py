'''
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges/
'''
import collections
import itertools
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        n_orange = sum(1 for cell in sum(grid, []) if cell != 0)

        queue = collections.deque()
        for x, y in itertools.product(range(m), range(n)):
            if grid[x][y] == 2:
                queue.append((x, y))

        offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        res = 0

        while queue:
            size = len(queue)
            for _ in range(size):
                x, y = queue.popleft()
                n_orange -= 1
                for dx, dy in offset:
                    if not 0 <= x + dx < m or not 0 <= y + dy < n:
                        continue
                    if grid[x + dx][y + dy] in [0, 2]:
                        continue
                    grid[x + dx][y + dy] = 2
                    queue.append((x + dx, y + dy))
            res += 1
        return max(0, res - 1) if not n_orange else -1
