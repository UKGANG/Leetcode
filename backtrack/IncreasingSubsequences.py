'''
491. Increasing Subsequences
https://leetcode.com/problems/increasing-subsequences/
'''
import collections
import functools
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if len(combo) > 1:
                res.append(combo[:])
            if start == len(nums):
                return

            seen = collections.Counter()
            for end in range(start, len(nums)):
                if combo and combo[-1] > nums[end]:
                    continue
                if seen[nums[end]]:
                    continue
                combo.append(nums[end])
                seen[nums[end]] += 1
                backtrack(end + 1)
                combo.pop()

        res, combo = [], []
        backtrack(0)
        return res
