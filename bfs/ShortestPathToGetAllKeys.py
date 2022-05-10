'''
864. Shortest Path to Get All Keys
https://leetcode.com/problems/shortest-path-to-get-all-keys/
'''
import itertools
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        x, y = 0, 0
        keys = [0] * 6

        for i, j in itertools.product(range(m), range(n)):
            if grid[i][j] == '@':
                x, y = i, j
            if grid[i][j].islower():
                keys[ord(grid[i][j]) - ord('a')] = 1
        keys = tuple(keys)

        curr_level = set([(x, y, tuple([0] * 6))])
        visited = set([(x, y, tuple([0] * 6))])

        res = 0
        while curr_level:
            res += 1
            next_level = set()
            for x, y, curr_keys in curr_level:
                direction = itertools.product([-1, 0, 1], [-1, 0, 1])
                direction = [(dx, dy) for dx, dy in direction if dx * dy == 0 and dx != dy]
                neighbor = [(x + dx, y + dy) for dx, dy in direction]
                neighbor = [(a, b) for a, b in neighbor if 0 <= a < m and 0 <= b < n]
                neighbor = [(a, b) for a, b in neighbor if grid[a][b] != '#']
                for next_x, next_y in neighbor:
                    next_keys = curr_keys
                    if grid[next_x][next_y].islower():
                        next_keys = list(next_keys)
                        next_keys[ord(grid[next_x][next_y]) - ord('a')] = 1
                        next_keys = tuple(next_keys)
                        if keys == next_keys:
                            return res
                    if grid[next_x][next_y].isupper():
                        if next_keys[ord(grid[next_x][next_y]) - ord('A')] == 0:
                            continue
                    if (next_x, next_y, next_keys) in visited:
                        continue
                    visited.add((next_x, next_y, next_keys))
                    next_level.add((next_x, next_y, next_keys))
            curr_level = next_level

        return -1


assert_value(8, Solution().shortestPathAllKeys, grid=[
    "@.a.#",
    "###.#",
    "b.A.B"
])
assert_value(6, Solution().shortestPathAllKeys, grid=[
    "@..aA",
    "..B#.",
    "....b"
])
