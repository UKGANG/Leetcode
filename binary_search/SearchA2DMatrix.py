'''
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix) - 1, 0
        while r >= 0 and c < len(matrix[0]):
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                c += 1
            else:
                r -= 1

        return False


assert_value(True, Solution().searchMatrix, matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
assert_value(False, Solution().searchMatrix, matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
