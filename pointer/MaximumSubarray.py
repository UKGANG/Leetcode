'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        m = len(nums) >> 1

        left_sub = nums[:m]
        right_sub = nums[m:]
        left = self.maxSubArray(left_sub)
        right = self.maxSubArray(right_sub)

        for i in reversed(range(len(left_sub) - 1)):
            left_sub[i] += left_sub[i + 1]

        for i in range(1, len(right_sub)):
            right_sub[i] += right_sub[i - 1]

        mid = max(left_sub) + max(right_sub)
        return max(left, right, mid)


assert_value(6, Solution().maxSubArray, nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
assert_value(1, Solution().maxSubArray, nums=[1])
assert_value(23, Solution().maxSubArray, nums=[5, 4, -1, 7, 8])
