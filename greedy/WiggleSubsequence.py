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

    def _wiggleMaxLength(self, nums: List[int]) -> int:
        dp_peek = [1] * len(nums)
        dp_lull = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                dp_peek[i] = dp_lull[i - 1] + 1
                dp_lull[i] = dp_lull[i - 1]
            elif nums[i - 1] > nums[i]:
                dp_lull[i] = dp_peek[i - 1] + 1
                dp_peek[i] = dp_peek[i - 1]
            else:
                dp_peek[i] = dp_peek[i - 1]
                dp_lull[i] = dp_lull[i - 1]

        return max(dp_peek[-1], dp_lull[-1])
