'''
377. Combination Sum IV
https://leetcode.com/problems/combination-sum-iv/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        m, n = len(nums), target

        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(1, n + 1):
            for j in range(m):
                if nums[j] > i:
                    continue
                dp[i] += dp[i - nums[j]]
        return dp[-1]
