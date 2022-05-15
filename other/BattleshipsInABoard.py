'''
419. Battleships in a Board
https://leetcode.com/problems/battleships-in-a-board/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res, m, n = 0, len(board), len(board[0])
        for i, j in itertools.product(range(m), range(n)):
            if board[i][j] == '.':
                continue
            if (i == 0 or board[i - 1][j] == '.') and (j == 0 or board[i][j - 1] == '.'):
                res += 1

        return res


assert_value(2, Solution().countBattleships, board=[["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]])
assert_value(0, Solution().countBattleships, board=[["."]])
