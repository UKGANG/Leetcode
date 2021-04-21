'''
1186. Maximum Subarray Sum with One Deletion
https://leetcode.com/problems/maximum-subarray-sum-with-one-deletion/
'''
from typing import List

from test_tool import assert_value


class Solution(object):
    def maximumSum(self, arr):
        if all(x <= 0 for x in arr):  # directly deal with corner case.
            return max(arr)
        n = len(arr)
        dp0 = list(arr)
        dp1 = [0] * n
        for i in range(1, n):
            dp0[i] = max(dp0[i - 1] + arr[i], arr[i])
            dp1[i] = max(dp1[i - 1] + arr[i], dp0[i - 1])
        return max(dp0 + dp1)


assert_value(4, Solution().maximumSum, arr=[1, -2, 0, 3])
assert_value(3, Solution().maximumSum, arr=[1, -2, -2, 3])
assert_value(-1, Solution().maximumSum, arr=[-1, -1, -1, -1])
assert_value(1, Solution().maximumSum, arr=[1, -1, -1, -1])
assert_value(20, Solution().maximumSum, arr=[-1, -2, -3, -4, -5, 20])
