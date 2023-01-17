"""
2016. Maximum Difference Between Increasing Elements
https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
"""
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        prev_min = nums[0]
        for i in range(len(nums)):
            res = max(res, nums[i] - prev_min)
            prev_min = min(prev_min, nums[i])
        return res if res else -1
