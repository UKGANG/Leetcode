"""
1034. Coloring A Border
https://leetcode.com/problems/coloring-a-border
"""
import collections
from typing import List


class Solution:
    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        border = set()
        queue = collections.deque([(row, col)])
        seen = set((row, col))
        source_color = grid[row][col]

        while queue:
            x, y = queue.popleft()
            for dx, dy in [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1),
            ]:
                _x, _y = x + dx, y + dy
                if not (0 <= _x < m and 0 <= _y < n and grid[_x][_y] == grid[row][col]):
                    border.add((x, y))
                    continue
                if (_x, _y) in seen:
                    continue
                seen.add((_x, _y))
                queue.append((_x, _y))

        for x, y in border:
            grid[x][y] = color
        return grid
