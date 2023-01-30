'''
494. Target Sum
https://leetcode.com/problems/target-sum/
'''
import collections
from collections import Counter
from typing import List

from test_tool import assert_value


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if total < target or (total - target) & 1:
            return 0
        target = (total - target) >> 1

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for sub_total in range(target, num - 1, -1):
                dp[sub_total] += dp[sub_total - num]
        return dp[-1]

    def _findTargetSumWays(self, nums: List[int], target: int) -> int:
        zeros = sum(1 for num in nums if not num)
        nums = [num for num in nums if num]
        m, n = len(nums), sum(nums)

        if abs(target) > n or (target + n) & 1:
            return 0

        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        for i in range(m + 1):
            dp[i][0] = 1

        nums.insert(0, None)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] += dp[i - 1][j]
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i]]

        return dp[-1][(target + n) >> 1] * 2 ** zeros

    def __findTargetSumWays(self, nums: List[int], target: int) -> int:
        m, n = len(nums), sum(nums)
        dp = {}
        if nums[0]:
            dp[nums[0]] = dp[-nums[0]] = 1
        else:
            dp[0] = 2
        for i in range(1, m):
            dp_next = {}
            for j in range(n, -n - 1, -1):
                dp_next[j] = dp_next.get(j, 0)
                dp_next[j] += dp.get(j - nums[i], 0)
                dp_next[j] += dp.get(j + nums[i], 0)
            dp = dp_next

        return dp.get(target, 0)

    def ___findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic[d]
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic[d]
            dic = tdic
        return dic.get(target, 0)


assert_value(5, Solution().findTargetSumWays, nums=[1, 1, 1, 1, 1], target=3)
assert_value(1, Solution().findTargetSumWays, nums=[1], target=1)
