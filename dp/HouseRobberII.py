'''
213. House Robber II
https://leetcode.com/problems/house-robber-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        # 1 ~ (n - 1)
        dp1 = [None] * (len(nums) - 1)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])

        # 2 ~ (n)
        dp2 = [None] * (len(nums) - 1)
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i + 1])

        return max(dp1[len(dp1) - 1], dp2[len(dp2) - 1])


assert_value(3, Solution().rob, nums=[2, 3, 2])
assert_value(4, Solution().rob, nums=[1, 2, 3, 1])
