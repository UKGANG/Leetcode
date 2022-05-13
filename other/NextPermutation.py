'''
31. Next Permutation
https://leetcode.com/problems/next-permutation/
'''
from typing import List

import numpy

from test_tool import assert_value


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums = nums.copy()
        if len(nums) < 2:
            return nums
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] >= nums[i]:
                continue
            head = i - 1
            min_j = nums[head]
            tail = head + 1
            for i in range(head + 1, len(nums)):
                if nums[tail] >= nums[i] > min_j:
                    tail = i
            nums[head], nums[tail] = nums[tail], nums[head]

            for i in range((len(nums) - head - 1) >> 1):
                nums[head + 1 + i], nums[len(nums) - 1 - i] = nums[len(nums) - 1 - i], nums[head + 1 + i]
            break
        else:
            nums.reverse()
        return nums


assert_value([1, 3, 2], Solution().nextPermutation, nums=[1, 2, 3])
assert_value([1, 2, 3], Solution().nextPermutation, nums=[3, 2, 1])
assert_value([1, 5, 1], Solution().nextPermutation, nums=[1, 1, 5])
assert_value([2, 1, 3], Solution().nextPermutation, nums=[1, 3, 2])
assert_value([2, 3, 3, 1, 3], Solution().nextPermutation, nums=[2, 3, 1, 3, 3])
