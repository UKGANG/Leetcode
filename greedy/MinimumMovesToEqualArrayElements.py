"""
453. Minimum Moves to Equal Array Elements
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/
"""
from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        return sum(nums) - len(nums) * min(nums)

    def _minMoves(self, nums: List[int]) -> int:
        nums.sort()
        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
        res = curr = 0
        for d in diff:
            curr += d
            res += curr

        return res
