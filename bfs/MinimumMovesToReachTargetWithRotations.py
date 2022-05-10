'''
1210. Minimum Moves to Reach Target with Rotations
https://leetcode.com/problems/minimum-moves-to-reach-target-with-rotations/
'''
import collections
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        if not grid or grid[0][0] or grid[0][1] or grid[-1][-1]:
            return -1
        m, n = len(grid), len(grid[0])
        visited = set([(0, 1, 0, 0)])
        curr_level = set([(0, 1, 0, 0)])
        res = 0
        while curr_level:
            next_level = set()
            for head_x, head_y, tail_x, tail_y in curr_level:
                if (head_x, head_y, tail_x, tail_y) == (m - 1, n - 1, m - 1, n - 2):
                    return res
                is_horizontal = head_x == tail_x

                move = [
                    (head_x, head_y + 1, head_x, head_y),
                    (tail_x + 1, tail_y, tail_x, tail_y),
                    (head_x + 1, head_y, tail_x + 1, tail_y),
                ] if is_horizontal else [
                    (head_x + 1, head_y, head_x, head_y),
                    (tail_x, tail_y + 1, tail_x, tail_y),
                    (head_x, head_y + 1, tail_x, tail_y + 1),
                ]
                move = [
                    (next_head_x, next_head_y, next_tail_x, next_tail_y)
                    for next_head_x, next_head_y, next_tail_x, next_tail_y in move
                    if 0 <= next_head_x < m
                       and 0 <= next_head_y < n
                       and grid[next_head_x][next_head_y] == 0
                       and grid[next_tail_x][next_tail_y] == 0
                       and (next_head_x, next_head_y, next_tail_x, next_tail_y) not in visited
                ]
                move = [
                    (next_head_x, next_head_y, next_tail_x, next_tail_y)
                    for next_head_x, next_head_y, next_tail_x, next_tail_y in move
                    if (next_tail_x, next_tail_y) != (tail_x, tail_y)
                       or grid[next_tail_x + 1][next_tail_y + 1] == 0
                ]
                for next_head_x, next_head_y, next_tail_x, next_tail_y in move:
                    next_level.add((next_head_x, next_head_y, next_tail_x, next_tail_y))
                    visited.add((next_head_x, next_head_y, next_tail_x, next_tail_y))
            curr_level = next_level
            res += 1

        return -1


assert_value(3, Solution().minimumMoves, grid=[
    [0, 0, 0],
    [1, 0, 0],
    [0, 0, 0],
])
assert_value(11, Solution().minimumMoves, grid=[
    [0, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0]
])
assert_value(9, Solution().minimumMoves, grid=[
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1],
    [1, 1, 1, 0, 0, 0]
])

assert_value(-1, Solution().minimumMoves, grid=[
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])
