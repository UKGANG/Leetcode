'''
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1


assert_value([1, 3, 12, 0, 0], Solution().moveZeroes, nums=[0, 1, 0, 3, 12])
assert_value([0], Solution().moveZeroes, nums=[0])
