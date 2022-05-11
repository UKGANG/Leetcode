'''
1263. Minimum Moves to Move a Box to Their Target Location
https://leetcode.com/problems/minimum-moves-to-move-a-box-to-their-target-location/
'''
import collections
import heapq
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        x_person, y_person, x_box, y_box, x_target, y_target = 0, 0, 0, 0, 0, 0
        for x, y in itertools.product(range(m), range(n)):
            if grid[x][y] == 'S':
                grid[x][y] == '.'
                x_person, y_person = x, y
            elif grid[x][y] == 'B':
                grid[x][y] == '.'
                x_box, y_box = x, y
            elif grid[x][y] == 'T':
                x_target, y_target = x, y

        curr_level = [(0, x_person, y_person, x_box, y_box)]
        visited = set([(x_person, y_person, x_box, y_box)])
        while curr_level:
            n_push, curr_x_person, curr_y_person, curr_x_box, curr_y_box = heapq.heappop(curr_level)
            move = itertools.product([-1, 0, 1], [-1, 0, 1])
            move = [(dx, dy) for dx, dy in move if dx * dy == 0 and dx != dy]
            move = [(curr_x_person + dx, curr_y_person + dy) for dx, dy in move]
            move = [
                (next_x_person, next_y_person)
                for next_x_person, next_y_person in move
                if 0 <= next_x_person < m
                   and 0 <= next_y_person < n
                   and grid[next_x_person][next_y_person] != '#'
            ]
            move = [
                (next_x_person, next_y_person)
                for next_x_person, next_y_person in move
                if 0 <= next_x_person < m
                   and 0 <= next_y_person < n
                   and grid[next_x_person][next_y_person] != '#'
            ]
            for next_x_person, next_y_person in move:
                n_push_next = n_push
                next_x_box, next_y_box = curr_x_box, curr_y_box
                if (next_x_person, next_y_person) == (curr_x_box, curr_y_box):
                    if curr_x_person == next_x_person:
                        next_y_box += 1 if curr_y_person < next_y_person else -1
                    else:
                        next_x_box += 1 if curr_x_person < next_x_person else -1
                if not (0 <= next_x_box < m and 0 <= next_y_box < n):
                    continue
                if (next_x_person, next_y_person, next_x_box, next_y_box) in visited:
                    continue
                if (next_x_person, next_y_person) == (curr_x_box, curr_y_box):
                    n_push_next += 1
                if (next_x_box, next_y_box) == (x_target, y_target):
                    return n_push_next
                visited.add((next_x_person, next_y_person, next_x_box, next_y_box))

                heapq.heappush(curr_level, (n_push_next, next_x_person, next_y_person, next_x_box, next_y_box))

        return -1


assert_value(3, Solution().minPushBox, grid=[
    ["#", "#", "#", "#", "#", "#"],
    ["#", "T", "#", "#", "#", "#"],
    ["#", ".", ".", "B", ".", "#"],
    ["#", ".", "#", "#", ".", "#"],
    ["#", ".", ".", ".", "S", "#"],
    ["#", "#", "#", "#", "#", "#"]
])
assert_value(-1, Solution().minPushBox, grid=[
    ["#", "#", "#", "#", "#", "#"],
    ["#", "T", "#", "#", "#", "#"],
    ["#", ".", ".", "B", ".", "#"],
    ["#", "#", "#", "#", ".", "#"],
    ["#", ".", ".", ".", "S", "#"],
    ["#", "#", "#", "#", "#", "#"]
])
assert_value(5, Solution().minPushBox, grid=[
    ["#", "#", "#", "#", "#", "#"],
    ["#", "T", ".", ".", "#", "#"],
    ["#", ".", "#", "B", ".", "#"],
    ["#", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", "S", "#"],
    ["#", "#", "#", "#", "#", "#"]
])
assert_value(7, Solution().minPushBox, grid=[
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "#", ".", ".", ".", ".", "."],
    [".", "T", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", "#", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "S", ".", "B", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."]
])
assert_value(5, Solution().minPushBox, grid=[
    [".", ".", "#", ".", ".", ".", ".", ".", ".", "."],
    [".", "#", ".", "#", "B", "#", ".", "#", ".", "."],
    [".", "#", ".", ".", ".", ".", ".", ".", "T", "."],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    [".", ".", ".", ".", ".", ".", ".", ".", "#", "."],
    [".", ".", ".", "#", ".", ".", "#", "#", ".", "."],
    [".", ".", ".", ".", "#", ".", ".", "#", ".", "."],
    [".", "#", ".", "S", ".", ".", ".", ".", ".", "."],
    ["#", ".", ".", "#", ".", ".", ".", ".", ".", "#"]
])
