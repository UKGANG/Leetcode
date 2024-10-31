'''
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, -float('inf'))
        nums.append(-float('inf'))
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
                return i - 1

        return len(nums) - 3

    def _findPeakElement(self, nums: List[int]) -> int:
        return self._find(nums, 0, len(nums) - 1)

    def _find(self, nums: List[int], l: int, r: int) -> int:
        if l + 1 == r:
            if nums[l] > nums[r]:
                return l
            return r
        if l == r:
            return l

        m = (l + r) >> 1
        if nums[m - 1] < nums[m] and nums[m + 1] < nums[m]:
            return m

        if nums[m - 1] > nums[m + 1]:
            return self._find(nums, l, m)
        return self._find(nums, m, r)

    def __findPeakElement(self, nums: List[int]) -> int:
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        for i in range(1, len(diff)):
            if diff[i - 1] > 0 and diff[i] < 0:
                return i

        if nums[0] > nums[-1]:
            return 0
        return len(nums) - 1


assert_value(2, Solution().findPeakElement, nums=[1, 2, 3, 1])
assert_value(5, Solution().findPeakElement, nums=[1, 2, 1, 3, 5, 6, 4])
