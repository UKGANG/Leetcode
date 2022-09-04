'''
718. Maximum Length of Repeated Subarray
https://leetcode.com/problems/maximum-length-of-repeated-subarray/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)

        dp = [
            [0] * n
            for _ in range(m)
        ]

        res = 0
        for i in range(m):
            for j in range(n):
                if nums1[i] != nums2[j]:
                    continue
                dp[i][j] = 1 + (dp[i - 1][j - 1] if i > 0 and j > 0 else 0)
                res = max(res, dp[i][j])

        return res

    def _greedy_findLength(self, nums1: List[int], nums2: List[int]) -> int:

        nums2_str = ''.join([chr(x) for x in nums2])
        max_str = ''
        res = 0
        for num in nums1:
            max_str += chr(num)
            if max_str in nums2_str:
                res = max(res, len(max_str))
            else:
                max_str = max_str[1:]

        return res
