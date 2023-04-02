"""
1755. Closest Subsequence Sum
https://leetcode.com/problems/closest-subsequence-sum
"""
import bisect
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        leftCombo, rightCombo = [0], [0]

        for i in range(n >> 1):
            size = len(leftCombo)
            for j in range(size):
                leftCombo.append(nums[i] + leftCombo[j])
        for i in range(n >> 1, n):
            size = len(rightCombo)
            for j in range(size):
                rightCombo.append(nums[i] + rightCombo[j])

        leftCombo = sorted(list(set(leftCombo)))
        rightCombo = list(set(rightCombo))

        res = float('inf')

        for rightSum in rightCombo:
            remaining = goal - rightSum
            idx = bisect.bisect(leftCombo, remaining)
            leftSum = leftCombo[idx] if idx < len(leftCombo) else leftCombo[-1]
            if remaining == leftSum:
                return 0
            res = min(res, abs(goal - leftSum - rightSum))

            idx -= 1
            leftSum = leftCombo[idx] if idx > -1 else leftCombo[0]
            res = min(res, abs(goal - leftSum - rightSum))
        return res
