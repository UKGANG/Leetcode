"""
48. Rotate Image
https://leetcode.com/problems/rotate-image
"""
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        top = left = 0
        bottom = right = n - 1

        prev = [0] * n
        curr = [0] * n
        while top <= bottom and left <= right:

            length = bottom - top
            for idx, i in enumerate(range(bottom, top, -1)):
                prev[idx] = matrix[i][left]
            for idx, i in enumerate(range(left, right)):
                curr[idx] = matrix[top][i]
                matrix[top][i] = prev[idx]

            prev[:length + 1] = curr[:length + 1]
            for idx, i in enumerate(range(top, bottom)):
                curr[idx] = matrix[i][right]
                matrix[i][right] = prev[idx]

            prev[:length + 1] = curr[:length + 1]
            for idx, i in enumerate(range(right, left, -1)):
                curr[idx] = matrix[bottom][i]
                matrix[bottom][i] = prev[idx]

            prev[:length + 1] = curr[:length + 1]
            for idx, i in enumerate(range(bottom, top, -1)):
                curr[idx] = matrix[i][left]
                matrix[i][left] = prev[idx]

            top += 1
            bottom -= 1
            left += 1
            right -= 1
