'''
376. Wiggle Subsequence
https://leetcode.com/problems/wiggle-subsequence/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prev_diff = None
        res = 1
        for i in range(1, len(nums)):
            curr_diff = nums[i] - nums[i - 1]
            if not prev_diff:
                prev_diff = curr_diff
                if curr_diff:
                    res += 1
                continue
            if curr_diff * prev_diff < 0:
                res += 1
                prev_diff = curr_diff

        return res
