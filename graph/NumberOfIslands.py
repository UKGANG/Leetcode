'''
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
'''
import itertools
from typing import List, Dict, Tuple

from test_tool import assert_value


class UnionFind:

    def __init__(self):
        self._cache: Dict[Tuple[int, int], Tuple[int, int]] = dict()

    def create(self, x, y):
        self._cache[(x, y)] = (x, y)

    def find(self, x, y) -> Tuple[int, int]:
        while (x, y) != self._cache[(x, y)]:
            x, y = self._cache[(x, y)]
        return x, y

    def union(self, x_1, y_1, x_2, y_2):
        root_x_1, root_y_1 = self.find(x_1, y_1)  # O(m + n)
        root_x_2, root_y_2 = self.find(x_2, y_2)  # O(m + n)

        if (root_x_1, root_y_1) == (root_x_2, root_y_2):
            return
        self._cache[(root_x_2, root_y_2)] = (root_x_1, root_y_1)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        stack = []
        res = 0
        offset = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
        ]
        for x, y in itertools.product(range(m), range(n)):
            if grid[x][y] == '0':
                continue
            res += 1
            stack.append((x, y))
            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for _x, _y in offset:
                    _x += x
                    _y += y
                    if not (0 <= _x < m and 0 <= _y < n) or grid[_x][_y] == '0':
                        continue
                    stack.append((_x, _y))
        return res

    def numIslands_v1(self, grid: List[List[str]]) -> int:
        disjointed_set: UnionFind = UnionFind()

        # 1. Initialize grid using each coordination
        m, n = len(grid), len(grid[0])

        for x, y in itertools.product(range(m), range(n)):
            if grid[x][y] == '0':
                continue
            disjointed_set.create(x, y)  # O(m * n)

        # 2. Iterate over each coordination to join different group together
        for row in range(m):
            for col in range(n):  # O(m * n)
                # 2.1. If we found water, skip
                if grid[row][col] == '0':
                    continue
                # 2.2. Check its adjacent coordination
                if col < n - 1 and grid[row][col + 1] == '1':
                    # 2.3. Merge it if necessary
                    disjointed_set.union(row, col, row, col + 1)  # O(m + n)
                if row < m - 1 and grid[row + 1][col] == '1':
                    # 2.3. Merge it if necessary
                    disjointed_set.union(row, col, row + 1, col)  # O(m + n)

        res = set()
        for x, y in itertools.product(range(m), range(n)):  # O(m * n)
            if grid[x][y] == '0':
                continue
            root = disjointed_set.find(x, y)  # O(m + n)
            res.add(root)

        return len(res)

    def numIslands_v0(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0
        accessed = [[False] * n for _ in range(m)]

        for i in range(len(accessed)):
            for j in range(len(accessed[0])):
                if accessed[i][j]:
                    continue
                if '0' == grid[i][j]:
                    accessed[i][j] = True
                    continue
                cnt += 1
                self.dfs(grid, accessed, i, j)
        return cnt

    def dfs(self, grid, accessed, i, j):
        m, n = len(grid), len(grid[0])
        curr_queue = [(i, j)]
        offset = itertools.product([-1, 0, 1], [-1, 0, 1])
        offset = [(di, dj) for di, dj in offset if bool(di) != bool(dj)]
        while curr_queue:
            i, j = curr_queue.pop()
            accessed[i][j] = True
            move = [(i + di, j + dj) for di, dj in offset]
            move = [(x, y) for x, y in move if 0 <= x < m and 0 <= y < n]
            move = [(x, y) for x, y in move if not accessed[x][y] and grid[x][y] == '1']
            for x, y in move:
                curr_queue.append((x, y))


assert_value(1, Solution().numIslands, grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])

assert_value(3, Solution().numIslands, grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])

assert_value(1, Solution().numIslands, grid=[
    ["1", "1", "1"],
    ["0", "1", "0"],
    ["1", "1", "1"]
])

assert_value(3, Solution().numIslands, grid=[
    ["1", "0", "1", "1", "0", "1", "1"]
])
