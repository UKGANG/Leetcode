'''
773. Sliding Puzzle
https://leetcode.com/problems/sliding-puzzle/
'''
import itertools
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        m, n = len(board), len(board[0])
        x, y = 0, 0
        for i, j in itertools.product(range(m), range(n)):
            if board[i][j] == 0:
                x, y = i, j
                break

        visited = set()
        res = 0
        curr_level = {(x, y, self.to_tuple(board))}
        ans = [[0] * n for _ in range(m)]
        for idx, (i, j) in enumerate(itertools.product(range(m), range(n))):
            ans[i][j] = idx + 1
        ans[-1][-1] = 0
        ans = self.to_tuple(ans)

        while curr_level:
            next_level = set()
            for i, j, board_tuple in curr_level:
                if board_tuple == ans:
                    return res
                visited.add(board_tuple)
                direction = [(dx, dy) for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1])]
                direction = [(dx, dy) for dx, dy in direction if dx * dy == 0 and dx != dy]
                move = [(i + dx, j + dy) for dx, dy in direction]
                move = [(x, y) for x, y in move if 0 <= x < m and 0 <= y < n]
                board_list = self.to_list(board_tuple)
                for x, y in move:
                    board_list[i][j], board_list[x][y] = board_list[x][y], board_list[i][j]
                    try:
                        board_tuple = self.to_tuple(board_list)
                        if board_tuple in visited:
                            continue
                        next_level.add((x, y, board_tuple))
                    finally:
                        board_list[i][j], board_list[x][y] = board_list[x][y], board_list[i][j]
            curr_level = next_level
            res += 1
        return -1

    def to_tuple(self, board: List[List[int]]) -> str:
        res = []
        for row in board:
            res.append(tuple(row))
        return tuple(res)

    def to_list(self, board: Tuple[Tuple[int]]) -> str:
        res = []
        for row in board:
            res.append(list(row))
        return res


assert_value(1, Solution().slidingPuzzle, board=[[1, 2, 3], [4, 0, 5]])
assert_value(-1, Solution().slidingPuzzle, board=[[1, 2, 3], [5, 4, 0]])
assert_value(5, Solution().slidingPuzzle, board=[[4, 1, 2], [5, 0, 3]])
