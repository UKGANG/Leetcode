'''
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx_1, idx_2 = m - 1, n - 1
        idx = len(nums1) - 1
        while idx_1 > -1 and idx_2 > -1 and m and n:
            if nums1[idx_1] > nums2[idx_2]:
                nums1[idx] = nums1[idx_1]
                idx_1 -= 1
                m -= 1
            else:
                nums1[idx] = nums2[idx_2]
                idx_2 -= 1
                n -= 1
            idx -= 1

        nums1[:n] = nums2[:n]

        return nums1


assert_value([1, 2, 2, 3, 5, 6], Solution().merge, nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3)
assert_value([1], Solution().merge, nums1=[1], m=1, nums2=[], n=0)
assert_value([1], Solution().merge, nums1=[0], m=0, nums2=[1], n=1)
assert_value([1, 2], Solution().merge, nums1=[2, 0], m=1, nums2=[1], n=1)
