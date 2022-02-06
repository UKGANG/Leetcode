'''
118. Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            row = []
            for j in range(-1, len(res[-1])):
                left = 0 if j == -1 else res[-1][j]
                right = 0 if j + 1 == len(res[-1]) else res[-1][j + 1]

                row.append(left + right)

            res.append(row)
        return res


assert_value([[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], Solution().generate, numRows=5)
assert_value([[1]], Solution().generate, numRows=1)
