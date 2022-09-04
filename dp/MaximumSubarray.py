'''
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        dp = [0] * n

        dp[0] = nums[0]

        for i in range(1, n):
            dp[i] = nums[i] + max(dp[i - 1], 0)

        return max(dp)

    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + dp[i], dp[i])
        return max(dp)

    def _divide_councer_revised_maxSubArray(self, nums: List[int]) -> int:
        def get_max(l, r):
            if l + 1 == r:
                return nums[l]
            m = (l + r) >> 1
            left = get_max(l, m)
            right = get_max(m, r)

            left_sub = float('-inf')
            curr = 0
            for i in range(m - 1, l - 1, -1):
                curr += nums[i]
                left_sub = max(left_sub, curr)

            right_sub = float('-inf')
            curr = 0
            for i in range(m, r):
                curr += nums[i]
                right_sub = max(right_sub, curr)

            return max(left, right, left_sub + right_sub)

        return get_max(0, len(nums))

    def _divide_councer_maxSubArray(self, nums: List[int]) -> int:
        def sub_max(i, j):
            if i == j:
                return None
            if i + 1 == j:
                return nums[i]
            m = (i + j) >> 1
            max_sub_left = sub_max(i, m)
            max_sub_right = sub_max(m, j)
            max_left = None
            max_right = None
            if i < m:
                curr = nums[m - 1]
                max_left = curr
                for k in range(m - 2, i - 1, -1):
                    curr += nums[k]
                    max_left = max(max_left, curr)
            if m < j:
                curr = nums[m]
                max_right = curr
                for k in range(m + 1, j):
                    curr += nums[k]
                    max_right = max(max_right, curr)
            max_left = max_left if max_left else 0
            max_right = max_right if max_right else 0
            max_mid = max_left + max_right
            return max(res for res in (max_sub_left, max_sub_right, max_mid) if res is not None)

        return sub_max(0, len(nums))

    def _greddy_revised_maxSubArray(self, nums: List[int]) -> int:
        res = float('-inf')
        curr = 0

        for num in nums:
            curr += num
            res = max(res, curr, num)
            curr = max(curr, 0)

        return res

    def _greddy_maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]
        for i in range(1, len(nums)):
            curr = max(curr + nums[i], nums[i])
            res = max(res, curr)
        return res


assert_value(4, Solution().maxSubArray, nums=[-2, 1, -3, 4])
assert_value(6, Solution().maxSubArray, nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
