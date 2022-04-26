'''
2128. Remove All Ones With Row and Column Flips
https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        pattern, pattern_reverse = grid[0], [1 - i for i in grid[0]]
        for idx in range(1, len(grid)):
            if grid[idx] != pattern and grid[idx] != pattern_reverse:
                return False
        return True


assert_value(True, Solution().removeOnes, grid=[[0, 1, 0], [1, 0, 1], [0, 1, 0]])
assert_value(False, Solution().removeOnes, grid=[[1, 1, 0], [0, 0, 0], [0, 0, 0]])
assert_value(True, Solution().removeOnes, grid=[[0]])
