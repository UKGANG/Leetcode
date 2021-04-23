'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m = int(len(nums) / 2)

        if len(nums) == 1:
            return nums[0]

        left = self.maxSubArray(nums[:m])
        right = self.maxSubArray(nums[m:])
        mid_left_arr = nums[:m]
        mid_right_arr = nums[m:]
        for idx in reversed(range(len(mid_left_arr) - 1)):
            mid_left_arr[idx] += mid_left_arr[idx + 1]
        for idx in range(1, len(mid_right_arr)):
            mid_right_arr[idx] += mid_right_arr[idx - 1]

        mid = max(mid_left_arr) + max(mid_right_arr)

        return max(left, right, mid)


assert_value(4, Solution().maxSubArray, nums=[-2, 1, -3, 4])
assert_value(6, Solution().maxSubArray, nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
