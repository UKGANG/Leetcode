"""
529. Minesweeper
https://leetcode.com/problems/minesweeper/description/
"""
import collections
from typing import List


class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        clicks = collections.deque([click])
        while clicks:
            x, y = clicks.popleft()
            if board[x][y] == 'M':
                board[x][y] = 'X'
                return board
            if board[x][y] != 'E':
                continue
            mark = 0
            next_click = []
            for dx, dy in itertools.product([-1, 0, 1], [-1, 0, 1]):
                if dx == dy == 0:
                    continue
                _x, _y = x + dx, y + dy
                if not 0 <= _x < m or not 0 <= _y < n:
                    continue
                if board[_x][_y] == 'M':
                    mark += 1
                    continue
                if board[_x][_y] == 'E':
                    next_click.append([_x, _y])
            board[x][y] = f'{mark}' if mark else 'B'
            if not mark:
                clicks.extend(next_click)

        return board
