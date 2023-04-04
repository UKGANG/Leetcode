"""
189. Rotate Array
https://leetcode.com/problems/rotate-array
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def flip(nums, left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k %= n

        flip(nums, 0, n - 1)
        flip(nums, 0, k - 1)
        flip(nums, k, n - 1)
