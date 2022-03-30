'''
348. Design Tic-Tac-Toe
https://leetcode.com/problems/design-tic-tac-toe/
'''
from typing import List, Optional

from test_tool import assert_value


class Record:
    def __init__(self, n):
        self.diag_p = n
        self.diag_n = n
        self.row = {i: n for i in range(n)}
        self.col = {i: n for i in range(n)}


class TicTacToe:

    def __init__(self, n: int):
        self._n = n
        self._player_record = collections.defaultdict(lambda: Record(n))

    def move(self, row: int, col: int, player: int) -> int:
        # record the current placement.
        self._player_record[player].row[row] -= 1
        self._player_record[player].col[col] -= 1
        if row == col:
            self._player_record[player].diag_p -= 1
        if row + col == self._n - 1:
            self._player_record[player].diag_n -= 1

        if not self._player_record[player].row[row] \
                or not self._player_record[player].col[col] \
                or not self._player_record[player].diag_p \
                or not self._player_record[player].diag_n:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(3)
# assert_value(0, obj.move, row=0, col=0, player=1)
# assert_value(0, obj.move, row=0, col=2, player=2)
# assert_value(0, obj.move, row=2, col=2, player=1)
# assert_value(0, obj.move, row=1, col=1, player=2)
# assert_value(0, obj.move, row=2, col=0, player=1)
# assert_value(0, obj.move, row=1, col=0, player=2)
# assert_value(1, obj.move, row=2, col=1, player=1)

obj = TicTacToe(2)
assert_value(0, obj.move, row=0, col=1, player=1)
assert_value(0, obj.move, row=1, col=1, player=2)
assert_value(1, obj.move, row=1, col=0, player=1)

