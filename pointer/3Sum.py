'''
15. 3Sum
https://leetcode.com/problems/3sum/
'''
import itertools
import re
from typing import List

from test_tool import assert_value


class Solution:
    def _threeSum(self, nums: List[int]) -> List[List[int]]:
        cache = {}
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                total = nums[i] + nums[j]
                cache[total] = cache.get(total, set())
                cache[total].add(tuple(sorted([i, j])))

        res = set()
        for i in range(len(nums)):
            if -nums[i] not in cache:
                continue
            for first, second in cache[-nums[i]]:
                if first == i or second == i:
                    continue
                res.add(tuple(sorted([nums[first], nums[second], nums[i]])))
        res = [list(arr) for arr in res]
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for x in range(len(nums) - 2):
            if x and nums[x] == nums[x - 1]:
                continue
            y, z = x + 1, len(nums) - 1
            while y < z:
                s = nums[x] + nums[y] + nums[z]
                if s == 0:
                    res.append([nums[x], nums[y], nums[z]])
                    y += 1
                    z -= 1
                    while y < z and nums[y] == nums[y - 1]:
                        y += 1
                    while y < z and nums[z] == nums[z + 1]:
                        z -= 1
                elif s > 0:
                    z -= 1
                else:
                    y += 1

        return res


assert_value([[-1, -1, 2], [-1, 0, 1]], Solution().threeSum, nums=[-1, 0, 1, 2, -1, -4])
assert_value([], Solution().threeSum, nums=[])
assert_value([], Solution().threeSum, nums=[0])
assert_value([[-4, 2, 2]], Solution().threeSum, nums=[2, 2, -4])
