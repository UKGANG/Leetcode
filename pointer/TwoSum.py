'''
1. Two Sum
https://leetcode.com/problems/two-sum/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}

        for i, num in enumerate(nums):
            if target - num in cache:
                return [cache[target - num], i]

            cache[num] = i


assert_value([0, 1], Solution().twoSum, nums=[2, 7, 11, 15], target=9)
assert_value([1, 2], Solution().twoSum, nums=[3, 2, 4], target=6)
assert_value([0, 1], Solution().twoSum, nums=[3, 3], target=6)
