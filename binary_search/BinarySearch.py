'''
704. Binary Search
https://leetcode.com/problems/binary-search/
'''
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = l + ((r - l) >> 1)
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return l if nums[l] == target else -1