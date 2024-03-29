'''
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target & 1 or len(nums) == 1 or max(nums) > target >> 1:
            return False
        target >>= 1
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for n in range(target, num - 1, -1):
                dp[n] = dp[n] or dp[n - num]
            if dp[-1]:
                return True

        return False

    def _canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1 or len(nums) == 1 or max(nums) > total >> 1:
            return False

        dp = [
            [False] * ((total >> 1) + 1)
            for _ in range(len(nums) + 1)
        ]

        for i in range(len(dp)):
            dp[i][0] = True

        nums.insert(0, None)
        for i in range(1, len(dp)):
            num = nums[i]
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - num]
            if dp[i][-1]:
                return True
        return False
