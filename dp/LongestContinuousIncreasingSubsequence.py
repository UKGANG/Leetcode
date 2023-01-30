'''
674. Longest Continuous Increasing Subsequence
https://leetcode.com/problems/longest-continuous-increasing-subsequence/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left, right = 0, 1
        res = 1
        while right < len(nums):
            while right < len(nums) and nums[right - 1] < nums[right]:
                right += 1
            res = max(res, right - left)
            left, right = right, right + 1
        return res

    def _findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                continue
            dp[i] += dp[i - 1]

        return max(dp)

    def _greedy_findLengthOfLCIS(self, nums: List[int]) -> int:
        res = 1
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                curr = 1
                continue
            curr += 1
            res = max(res, curr)

        return res
