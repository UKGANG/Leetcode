'''
15. 3Sum
https://leetcode.com/problems/3sum/
'''
import itertools
import re
from typing import List

from test_tool import assert_value


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[l] + nums[r] + nums[i]
                if s == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1

        return result


assert_value([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum, nums=[-1, 0, 1, 2, -1, -4])
assert_value([], Solution().threeSum, nums=[])
assert_value([], Solution().threeSum, nums=[0])
assert_value([], Solution().threeSum, nums=[-4, 2, 2])
