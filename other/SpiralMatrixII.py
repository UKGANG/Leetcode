'''
59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        l, r, t, b = 0, n, 0, n
        matrix = [[0] * n for _ in range(n)]
        idx = 0
        x, y = 0, 0
        while l < r and t < b:
            for i in range(l, r):
                idx += 1
                matrix[x][i] = idx
            y = r - 1
            for i in range(t + 1, b):
                idx += 1
                matrix[i][y] = idx
            x = b - 1
            for i in range(r - 2, l - 1, -1):
                idx += 1
                matrix[x][i] = idx
            y = l
            for i in range(b - 2, t, -1):
                idx += 1
                matrix[i][y] = idx
            l += 1
            r -= 1
            t += 1
            b -= 1
            x, y = l, t

        return matrix


assert_value([[1, 2, 3], [8, 9, 4], [7, 6, 5]], Solution().generateMatrix, n=3)
assert_value([[1]], Solution().generateMatrix, n=1)
