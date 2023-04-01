"""
1775. Equal Sum Arrays With Minimum Number of Operations
https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations
"""
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums1) * 6 < len(nums2):
            return -1
        if len(nums2) * 6 < len(nums1):
            return -1
        sum1, sum2 = map(sum, (nums1, nums2))

        if sum1 > sum2:
            nums1, nums2 = nums2, nums1
            sum1, sum2 = sum2, sum1

        nums1, nums2 = map(sorted, (nums1, nums2))
        p1, p2 = 0, len(nums2) - 1

        res = 0
        while sum1 < sum2:
            diff1 = 6 - nums1[p1] if p1 < len(nums1) else 0
            diff2 = nums2[p2] - 1 if p2 > -1 else 0

            if diff1 > diff2:
                sum1 += diff1
                p1 += 1
            else:
                sum2 -= diff2
                p2 -= 1
            res += 1

        return res
