'''
167. Two Sum II - Input array is sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            res = numbers[l] + numbers[r]
            if res == target:
                return [l + 1, r + 1]
            if res > target:
                r -= 1
            if res < target:
                l += 1

    def _twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)
        while l < r:
            idx = self.findInsertIndex(numbers, target - numbers[l], l + 1, r)
            if numbers[idx - 1] == target - numbers[l]:
                return [l + 1, idx]
            l += 1
            r = idx

    def findInsertIndex(self, numbers, target, l, r):
        while l < r:
            m = (l + r) >> 1
            if numbers[m] <= target:
                l = m + 1
            else:
                r = m
        return r


assert_value([1, 2], Solution().twoSum, numbers=[2, 7, 11, 15], target=9)
assert_value([1, 3], Solution().twoSum, numbers=[2, 3, 4], target=6)
assert_value([1, 2], Solution().twoSum, numbers=[-1, 0], target=-1)
assert_value([1, 2], Solution().twoSum, numbers=[-1, 0], target=-1)
