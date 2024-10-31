"""
163. Missing Ranges
https://leetcode.com/problems/missing-ranges
"""
from typing import List

from test_tool import assert_value


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        nums.append(upper + 1)
        for upper in nums:
            if lower < upper:
                res.append([lower, upper - 1])
            lower = upper + 1
        return res
