'''
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Find the middle location.
        if len(nums) == 0:
            return [-1, -1]

        if nums[0] > target or nums[-1] < target:
            return [-1, -1]

        l, r = 0, len(nums)
        while l < r:
            m = (l + r) >> 1
            if nums[m] == target:
                l = m
                break
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1

        if nums[l] != target:
            return [-1, -1]
        mid = l

        # Find the head
        l, r = 0, mid
        while l < r:
            m = (l + r) >> 1
            if nums[m] < target:
                l = m + 1
            else:
                r = m

        left = l
        # Find the tail
        l, r = mid, len(nums)
        while l < r:
            m = (l + r) >> 1
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        return [left, l - 1]


assert_value([3, 4], Solution().searchRange, nums=[5, 7, 7, 8, 8, 10], target=8)
assert_value([-1, -1], Solution().searchRange, nums=[5, 7, 7, 8, 8, 10], target=6)
assert_value([-1, -1], Solution().searchRange, nums=[], target=0)
assert_value([0, 0], Solution().searchRange, nums=[1], target=1)
assert_value([0, 0], Solution().searchRange, nums=[1, 3], target=1)
assert_value([2, 5], Solution().searchRange, nums=[1, 2, 3, 3, 3, 3, 4, 5, 9], target=3)
