'''
435. Non-overlapping Intervals
https://leetcode.com/problems/non-overlapping-intervals/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        l ,r = intervals[-1]
        res = 0
        for i in range(len(intervals) - 2, -1, -1):
            if intervals[i][1] > l:
                res += 1
                continue
            l, r = intervals[i]

        return res


    def _eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda item: item[::-1])
        l, r = intervals[0]
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < r:
                res += 1
                continue
            l, r = intervals[i]
        return res
