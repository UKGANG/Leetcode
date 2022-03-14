'''
75. Sort Colors
https://leetcode.com/problems/sort-colors/
'''
import heapq
import itertools
import re
from typing import List

from test_tool import assert_value


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_0 = 0
        cnt_1 = 0
        cnt_2 = 0
        for n in nums:
            if n == 0:
                cnt_0 += 1
            elif n == 1:
                cnt_1 += 1
            else:
                cnt_2 += 1

        for i in range(cnt_0):
            nums[i] = 0
        for i in range(cnt_0, cnt_0 + cnt_1):
            nums[i] = 1
        for i in range(cnt_0 + cnt_1, len(nums)):
            nums[i] = 2

        return nums


assert_value([0, 0, 1, 1, 2, 2], Solution().sortColors, nums=[2, 0, 2, 1, 1, 0])
assert_value([0, 1, 2], Solution().sortColors, nums=[2, 0, 1])
