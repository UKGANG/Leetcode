"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        res = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                continue
            if nums[i - 1] + 1 == nums[i]:
                curr += 1
                res = max(res, curr)
                continue
            curr = 1

        return res
