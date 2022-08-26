'''
37. Sudoku Solver
https://leetcode.com/problems/sudoku-solver/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def backtrack():
            for row in range(9):
                for col in range(9):
                    if board[row][col] != '.':
                        continue
                    for n in range(1, 10):
                        if n in rows[row]:
                            continue
                        if n in cols[col]:
                            continue
                        if n in grid[row // 3 * 3 + col // 3]:
                            continue
                        rows[row].add(n)
                        cols[col].add(n)
                        grid[row // 3 * 3 + col // 3].add(n)
                        board[row][col] = str(n)
                        if backtrack():
                            return True
                        board[row][col] = '.'
                        rows[row].remove(n)
                        cols[col].remove(n)
                        grid[row // 3 * 3 + col // 3].remove(n)
                    return False
            return True

        rows = {n: set() for n in range(9)}
        cols = {n: set() for n in range(9)}
        grid = {n: set() for n in range(9)}
        for row in range(9):
            for col in range(9):
                n = board[row][col]
                if n != '.':
                    n = int(n)
                    rows[row].add(n)
                    cols[col].add(n)
                    grid[row // 3 * 3 + col // 3].add(n)

        backtrack()
