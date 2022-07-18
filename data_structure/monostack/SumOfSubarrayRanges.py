'''
2104. Sum of Subarray Ranges
https://leetcode.com/problems/sum-of-subarray-ranges/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ...

    def _subArrayRanges(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            v_max, v_min = nums[i], nums[i]
            for j in range(i, len(nums)):
                v_max = max(v_max, nums[j])
                v_min = min(v_min, nums[j])
                res += v_max - v_min

        return res


assert_value(4, Solution().subArrayRanges, nums=[1, 2, 3])
assert_value(4, Solution().subArrayRanges, nums=[1, 3, 3])
assert_value(59, Solution().subArrayRanges, nums=[4, -2, -3, 4, 1])
