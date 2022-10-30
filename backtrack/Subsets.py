'''
78. Subsets
https://leetcode.com/problems/subsets/
'''
import functools
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            for i in range(len(res)):
                res.append(res[i] + [num])
        return res

    def _subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, cnt):
            if not cnt:
                res.append(combo[:])
                return

            for i in range(start, len(nums)):
                combo.append(nums[i])
                backtrack(i + 1, cnt - 1)
                combo.pop()

        res, combo = [], []
        for n in range(len(nums) + 1):
            backtrack(0, n)
        return res
