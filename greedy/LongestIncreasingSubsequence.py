'''
300. Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
'''
import bisect
from typing import List

from test_tool import assert_value


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [nums[0]]
        for i in range(1, len(nums)):
            if lis[-1] < nums[i]:
                lis.append(nums[i])
                continue
            idx = bisect.bisect_left(lis, nums[i])
            lis[idx] = nums[i]
        return len(lis)

    def _lengthOfLIS(self, nums: List[int]) -> int:
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

    def _dp_lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


assert_value(4, Solution().lengthOfLIS, nums=[10, 9, 2, 5, 3, 7, 101])
assert_value(3, Solution().lengthOfLIS, nums=[4, 10, 4, 3, 8, 9])
