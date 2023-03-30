"""
154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + ((h - l) >> 1)
            if nums[m] < nums[h]:
                h = m
                continue
            if nums[m] > nums[h]:
                l = m + 1
                continue
            if nums[m] == nums[h]:
                h -= 1

        return nums[l]
