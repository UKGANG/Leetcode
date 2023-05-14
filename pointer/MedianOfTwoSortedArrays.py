"""
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays
"""
import bisect
from typing import List

from test_tool import assert_value


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m < n:
            return self.findMedianSortedArrays(nums2, nums1)
        for n2 in nums2:
            bisect.insort_right(nums1, n2)
        idx = (m + n) >> 1
        if (m + n) & 1:
            return nums1[idx]
        return (nums1[idx - 1] + nums1[idx]) / 2

    def _2_pointer_findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        p1 = p2 = 0
        arr = []
        while p1 <= m and p2 <= n:
            if p1 == m:
                nums1, p1, m, nums2, p2, n = nums2, p2, n, nums1, p1, m
            if p2 == n:
                if (m + n) & 1:
                    return nums1[((m + n) >> 1) - n]
                while len(arr) < ((m + n) >> 1) + 1:
                    arr.append(nums1[p1])
                    p1 += 1
                if (m + n) & 1:
                    return arr[-1]
                return sum(arr[-2:]) / 2

            if nums1[p1] < nums2[p2]:
                arr.append(nums1[p1])
                p1 += 1
            else:
                arr.append(nums2[p2])
                p2 += 1
            if len(arr) < ((m + n) >> 1) + 1:
                continue
            if (m + n) & 1:
                return arr[-1]
            return sum(arr[-2:]) / 2

    def _bf_findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        m = len(nums1) >> 1
        return nums1[m] if len(nums1) & 1 else (nums1[m - 1] + nums1[m]) / 2


assert_value(2, Solution().findMedianSortedArrays, nums1=[2], nums2=[1, 3])
assert_value(2, Solution().findMedianSortedArrays, nums1=[1, 3], nums2=[2])
assert_value(2.5, Solution().findMedianSortedArrays, nums1=[1, 2], nums2=[3, 4])
