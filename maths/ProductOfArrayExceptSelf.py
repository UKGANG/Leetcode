'''
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
'''
import heapq
from typing import List
from collections import defaultdict

from test_tool import assert_value


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        lp, rp = 1, 1
        for i in range(len(nums)):
            res[i] *= lp
            lp *= nums[i]
            res[~i] *= rp
            rp *= nums[~i]
        return res


assert_value([24, 12, 8, 6], Solution().productExceptSelf, nums=[1, 2, 3, 4])
assert_value([0, 0, 9, 0, 0], Solution().productExceptSelf, nums=[-1, 1, 0, -3, 3])
