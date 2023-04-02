"""
1578. Minimum Time to Make Rope Colorful
https://leetcode.com/problems/minimum-time-to-make-rope-colorful
"""
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = left = 0
        for right in range(1, len(colors)):
            if colors[left] != colors[right]:
                left = right
                continue
            if neededTime[left] < neededTime[right]:
                res += neededTime[left]
                left = right
            else:
                res += neededTime[right]
        return res
