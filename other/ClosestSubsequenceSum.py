"""
1755. Closest Subsequence Sum
https://leetcode.com/problems/closest-subsequence-sum
"""
import bisect
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        left_combo, right_combo = [0], [0]

        for i in range(n >> 1):
            size = len(left_combo)
            for j in range(size):
                left_combo.append(nums[i] + left_combo[j])
        for i in range(n >> 1, n):
            size = len(right_combo)
            for j in range(size):
                right_combo.append(nums[i] + right_combo[j])

        left_combo = sorted(list(set(left_combo)))
        right_combo = list(set(right_combo))

        res = float('inf')

        for right_sum in right_combo:
            remaining = goal - right_sum
            idx = bisect.bisect(left_combo, remaining)
            left_sum = left_combo[idx] if idx < len(left_combo) else left_combo[-1]
            if remaining == left_sum:
                return 0
            res = min(res, abs(goal - left_sum - right_sum))

            idx -= 1
            left_sum = left_combo[idx] if idx > -1 else left_combo[0]
            res = min(res, abs(goal - left_sum - right_sum))
        return res
