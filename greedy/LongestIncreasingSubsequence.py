'''
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [nums[0]]

        for idx in range(1, len(nums)):
            if dp[-1] < nums[idx]:
                dp.append(nums[idx])
                continue
            l, r = 0, len(dp) - 1
            loc = r
            while l <= r:
                m = (l + r) // 2
                if dp[m] >= nums[idx]:
                    loc = m
                    r = m - 1
                else:
                    l = m + 1
            dp[loc] = nums[idx]

        return len(dp)

    def lengthOfLIS_DP(self, nums: List[int]) -> int:
        dp = [0] * len(nums)

        for idx in range(len(nums)):
            dp[idx] = 1

            for i in range(idx):
                if nums[idx] > nums[i]:
                    dp[idx] = max(dp[idx], dp[i] + 1)
        return max(dp)


assert_value(4, Solution().lengthOfLIS, nums=[10, 9, 2, 5, 3, 7, 101])
assert_value(3, Solution().lengthOfLIS, nums=[4, 10, 4, 3, 8, 9])
