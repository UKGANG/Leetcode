"""
1283. Find the Smallest Divisor Given a Threshold
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold
"""
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def divisor_sum(divisor):
            result = 0
            for n in nums:
                val, resid = divmod(n, divisor)
                result += val
                result += 1 if resid else 0
            return result

        left, right = 1, max(nums)

        res = -1
        while left <= right:
            m = left + ((right - left) >> 1)
            result = divisor_sum(m)
            if result <= threshold:
                res = m
                right = m - 1
            else:
                left = m + 1

        return res
