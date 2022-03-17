'''
Leftmost column index of 1
https://leetcode.com/discuss/interview-question/341247/Facebook-or-Phone-screen-or-Leftmost-column-index-of-1
'''
from typing import List

from test_tool import assert_value


class Solution:
    def leftMost1(self, matrix: List[List[int]]) -> int:
        row, col = 0, len(matrix[0]) - 1
        res = -1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == 0:
                row += 1
            else:
                res = col
                col -= 1

        return res


assert_value(1, Solution().leftMost1, matrix=[[0, 0, 0, 1],
                                              [0, 0, 1, 1],
                                              [0, 1, 1, 1],
                                              [0, 0, 0, 0]])
assert_value(-1, Solution().leftMost1, matrix=[[0, 0, 0, 0],
                                               [0, 0, 0, 0],
                                               [0, 0, 0, 0],
                                               [0, 0, 0, 0]])
