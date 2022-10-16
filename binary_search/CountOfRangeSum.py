'''
327. Count of Range Sum
https://leetcode.com/problems/count-of-range-sum/
'''
from bisect import bisect
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res = 0
        curr = 0
        pre_sums = [0]
        for num in nums:
            curr += num
            lower_bound_idx = bisect.bisect_left(pre_sums, curr - upper)
            upper_bound_idx = bisect.bisect_right(pre_sums, curr - lower)
            res += upper_bound_idx - lower_bound_idx
            bisect.insort(pre_sums, curr)

        return res
