'''
766. Toeplitz Matrix
https://leetcode.com/problems/toeplitz-matrix/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m - 1):
            for j in range(n - 1):
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


assert_value(True, Solution().isToeplitzMatrix, matrix=[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
assert_value(False, Solution().isToeplitzMatrix, matrix=[[1, 2], [2, 2]])
