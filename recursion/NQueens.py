'''
51. N-Queens
https://leetcode.com/problems/n-queens/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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
