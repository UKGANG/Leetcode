'''
45. Jump Game II
https://leetcode.com/problems/jump-game-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        jump_range_curr, jump_range_max = 0, 0
        for i in range(len(nums)):

            jump_range_max = max(jump_range_max, i + nums[i])
            if i == jump_range_curr:
                res += 1
                jump_range_curr = jump_range_max
            if jump_range_curr >= len(nums) - 1:
                return res
        return None

    def _dp_jump(self, nums: List[int]) -> int:
        dp = [len(nums)] * len(nums)
        dp[0] = 0
        for i, n in enumerate(nums):
            for j in range(1, n + 1):
                if i + j > len(nums) - 1:
                    break
                dp[i + j] = min(dp[i + j], dp[i] + 1)
        return dp[-1]
