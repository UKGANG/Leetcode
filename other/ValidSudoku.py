'''
36. Valid Sudoku
https://leetcode.com/problems/valid-sudoku/
'''
import heapq
from typing import List
from collections import defaultdict

from test_tool import assert_value


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            if not self.check_arr(board[i]):
                return False

        for i in range(9):
            if not self.check_arr([board[j][i] for j in range(9)]):
                return False

        cache = [[0] * 9 for i in range(9)]
        for i in range(9):
            for j in range(9):
                if not board[i][j].isnumeric():
                    continue
                cache[i // 3 * 3 + j // 3][int(board[i][j]) - 1] += 1
                if cache[i // 3 * 3 + j // 3][int(board[i][j]) - 1] > 1:
                    return False
        return True

    def check_arr(self, arr: List[int]) -> bool:
        cache = [0] * 9
        for i in range(9):
            if arr[i].isnumeric():
                cache[int(arr[i]) - 1] += 1
                if cache[int(arr[i]) - 1] > 1:
                    return False
        return True


assert_value(True, Solution().isValidSudoku, board=[
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
])

assert_value(False, Solution().isValidSudoku, board=[
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
])

assert_value(False, Solution().isValidSudoku, board=[
    [".", ".", ".", ".", ".", ".", "5", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    ["9", "3", ".", ".", "2", ".", "4", ".", "."],
    [".", ".", "7", ".", ".", ".", "3", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "3", "4", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "."],
    [".", ".", ".", ".", ".", "5", "2", ".", "."],
])
