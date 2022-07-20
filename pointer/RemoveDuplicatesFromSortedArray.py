'''
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s, f = 0, 0
        while f < len(nums):
            if nums[s] != nums[f]:
                nums[s + 1] = nums[f]
                s += 1
            f += 1
        return s + 1


assert_value(2, Solution().removeDuplicates, nums=[1, 1, 2])
assert_value(5, Solution().removeDuplicates, nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
