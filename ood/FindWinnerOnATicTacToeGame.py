'''
1275. Find Winner on a Tic Tac Toe Game
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        board = [[None] * 3 for _ in range(3)]
        self.move('A', board, [moves[i] for i in range(0, len(moves), 2)])
        self.move('B', board, [moves[i] for i in range(1, len(moves), 2)])
        if self.check('A', board):
            return 'A'
        if self.check('B', board):
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'

    def move(self, char: str, board: List[List[int]], moves: List[List[int]]):
        for x, y in moves:
            board[x][y] = char

    def check(self, char: str, board: List[List[int]]):
        diag_cnt = 0
        diag_reverse_cnt = 0
        for i in range(3):
            row_cnt = 0
            col_cnt = 0
            if board[i][i] == char:
                diag_cnt += 1
            if board[2 - i][i] == char:
                diag_reverse_cnt += 1
            for j in range(3):
                if board[i][j] == char:
                    row_cnt += 1
                if board[j][i] == char:
                    col_cnt += 1
            if row_cnt == 3 or col_cnt == 3 or diag_cnt == 3 or diag_reverse_cnt == 3:
                return True
        return False


assert_value('A', Solution().tictactoe, moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]])
assert_value('B', Solution().tictactoe, moves=[[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]])
assert_value('Draw', Solution().tictactoe,
             moves=[[0, 0], [1, 1], [2, 0], [1, 0], [1, 2], [2, 1], [0, 1], [0, 2], [2, 2]])
assert_value('A', Solution().tictactoe, moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]])
assert_value('Pending', Solution().tictactoe, moves=[[0, 0], [1, 1]])
assert_value('Pending', Solution().tictactoe, moves=[[1, 1], [2, 0], [0, 2]])
assert_value('B', Solution().tictactoe, moves=[[2, 2], [0, 2], [1, 0], [0, 1], [2, 0], [0, 0]])
