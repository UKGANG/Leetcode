'''
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cache = {0: -1}
        res = 0

        accumulator = 0
        for idx, num in enumerate(nums):
            accumulator += 1 if num else -1
            if accumulator in cache:
                res = max(res, idx - cache[accumulator])
            else:
                cache[accumulator] = idx
        return res


assert_value(2, Solution().findMaxLength, nums=[0, 1])
assert_value(2, Solution().findMaxLength, nums=[0, 1, 0])
