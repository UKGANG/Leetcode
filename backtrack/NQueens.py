'''
51. N-Queens
https://leetcode.com/problems/n-queens/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            if row == n:
                combo = [['.'] * n for _ in range(n)]
                for col, row in cols.items():
                    combo[row][col] = 'Q'
                    combo[row] = ''.join(combo[row])
                res.append(combo)
                return
            for col in range(n):
                if col in cols:
                    continue
                if row + col in diags_reversed:
                    continue
                if row - col in diags:
                    continue
                cols[col] = row
                diags_reversed.add(row + col)
                diags.add(row - col)
                backtrack(row + 1)
                del cols[col]
                diags_reversed.remove(row + col)
                diags.remove(row - col)

        res = []
        cols = dict()
        diags, diags_reversed = set(), set()
        backtrack(0)
        return res

    def _solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row_2):
            if row_2 == n:
                res.append(queens[:])
                return
            for col_2 in range(n):
                valid = True
                for row_1, col_1 in queens:
                    slope = abs((row_1 - row_2) / (col_1 - col_2)) if col_1 - col_2 else float('inf')
                    if slope in [0, 1, float('inf')]:
                        valid = False
                        break
                if not valid:
                    continue
                queens.append((row_2, col_2))
                backtrack(row_2 + 1)
                queens.pop()

        res, queens = [], []
        backtrack(0)
        solutions = []
        for chesses in res:
            solution = [['.'] * n for _ in range(n)]
            for chess_x, chess_y in chesses:
                solution[chess_x][chess_y] = 'Q'
                solution[chess_x] = ''.join(solution[chess_x])
            solutions.append(solution)
        return solutions

    def __solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(i):
            if i == n:
                solution.append(list(curr_solution))
            else:
                for j in range(n):
                    if j not in col and j + i not in diag and j - i not in off_diag:
                        col.add(j)
                        diag.add(j + i)
                        off_diag.add(j - i)
                        curr_solution.append("." * j + "Q" + "." * (n - j - 1))
                        backtrack(i + 1)
                        curr_solution.pop()
                        col.remove(j)
                        diag.remove(j + i)
                        off_diag.remove(j - i)

        solution = []
        col = set()
        off_diag = set()
        diag = set()
        curr_solution = []
        backtrack(0)
        return solution


assert_value(
    [
        [
            ".Q..",
            "...Q",
            "Q...",
            "..Q."
        ],
        [
            "..Q.",
            "Q...",
            "...Q",
            ".Q.."
        ]
    ], Solution().solveNQueens, n=4
)
assert_value([["Q"]], Solution().solveNQueens, n=1)
