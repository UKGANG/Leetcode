'''
198. House Robber
https://leetcode.com/problems/house-robber/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n

        for i in range(n):
            dp[i] = max((dp[i - 2] if i > 1 else 0) + nums[i], dp[i - 1])
        return max(dp[-2:])
