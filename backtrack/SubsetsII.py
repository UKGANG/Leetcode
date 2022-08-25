'''
90. Subsets II
https://leetcode.com/problems/subsets-ii/
'''
import functools
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            res.append(combo[:])
            if start == len(nums):
                return
            for end in range(start, len(nums)):
                if end > start and nums[end] == nums[end - 1]:
                    continue
                combo.append(nums[end])
                backtrack(end + 1)
                combo.pop()

        nums = sorted(nums)
        res, combo = [], []
        backtrack(0)
        return res
