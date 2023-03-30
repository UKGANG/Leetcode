"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h = 0, len(nums) - 1
        while l < h:
            m = l + ((h - l) >> 1)
            if nums[m] < nums[h]:
                h = m
            else:
                l = m + 1
        return nums[l]
