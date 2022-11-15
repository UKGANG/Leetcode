'''
2018. Check if Word Can Be Placed In Crossword
https://leetcode.com/problems/check-if-word-can-be-placed-in-crossword/
'''
import itertools
from typing import List


class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        def is_valid_pos(x, y) -> bool:
            nonlocal m, n
            return 0 <= x < m and 0 <= y < n

        def is_vaild_place(x, y, d_pos) -> bool:
            for idx, s in enumerate(word):
                if not is_valid_pos(x, y) or board[x][y] == '#' or board[x][y] not in (' ', s):
                    return False
                x += d_pos[0]
                y += d_pos[1]
            return True

        m, n = len(board), len(board[0])
        len_word = len(word)

        for x, y in itertools.product(range(m), range(n)):
            if (not is_valid_pos(x, y - 1) or board[x][y - 1] == '#') and \
                    (not is_valid_pos(x, y + len_word) or board[x][y + len_word] == '#') and \
                    is_vaild_place(x, y, (0, 1)):
                return True
            if (not is_valid_pos(x, y + 1) or board[x][y + 1] == '#') and \
                    (not is_valid_pos(x, y - len_word) or board[x][y - len_word] == '#') and \
                    is_vaild_place(x, y, (0, -1)):
                return True

            if (not is_valid_pos(x - 1, y) or board[x - 1][y] == '#') and \
                    (not is_valid_pos(x + len_word, y) or board[x + len_word][y] == '#') and \
                    is_vaild_place(x, y, (1, 0)):
                return True
            if (not is_valid_pos(x + 1, y) or board[x + 1][y] == '#') and \
                    (not is_valid_pos(x - len_word, y) or board[x - len_word][y] == '#') and \
                    is_vaild_place(x, y, (-1, 0)):
                return True

        return False
