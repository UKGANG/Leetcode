'''
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
'''
import math
from typing import List

from test_tool import assert_value


class Solution:
    def _maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        m = len(nums) >> 1

        left_sub = nums[:m]
        right_sub = nums[m:]
        left = self.maxProduct(left_sub)
        right = self.maxProduct(right_sub)

        for i in reversed(range(len(left_sub) - 1)):
            left_sub[i] *= left_sub[i + 1]

        for i in range(1, len(right_sub)):
            right_sub[i] *= right_sub[i - 1]

        left_max = max(left_sub)
        left_min = min(left_sub)
        right_max = max(right_sub)
        right_min = min(right_sub)
        mid = left_max * right_max
        for l in [left_max, left_min]:
            for r in [right_max, right_min]:
                mid = max(mid, l * r)

        return max(left, right, mid)

    def __maxProduct(self, nums: List[int]) -> int:
        dp = [nums[0]]

        for num in nums[1:]:
            dp.append(max(num, dp[-1] * num))

        return max(dp)

    def maxProduct(self, nums: List[int]) -> int:
        maxi, mini, res = 1, 1, -math.inf

        for num in nums:
            acc_maxi = maxi * num
            acc_mini = mini * num
            maxi = max(num, acc_maxi, acc_mini)
            mini = min(num, acc_maxi, acc_mini)

            res = max(res, maxi)
        return res


assert_value(6, Solution().maxProduct, nums=[2, 3, -2, 4])
assert_value(0, Solution().maxProduct, nums=[-2, 0, -1])
assert_value(24, Solution().maxProduct, nums=[-2, 3, -4])
