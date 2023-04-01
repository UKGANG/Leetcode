"""
1822. Sign of the Product of an Array
https://leetcode.com/problems/sign-of-the-product-of-an-array
"""
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        res = 1
        for num in nums:
            if not num:
                return 0
            if num < 0:
                res *= -1
        return res
