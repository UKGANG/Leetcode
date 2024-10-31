'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start <= res[-1][-1]:
                res[-1][-1] = max(end, res[-1][-1])
            else:
                res.append([start, end])
        return res

    def _merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        l, r = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > r:
                res.append([l, r])
                l, r = intervals[i]
            else:
                r = max(r, intervals[i][1])
        res.append([l, r])
        return res

    def __merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if 1 >= len(intervals):
            return intervals
        intervals = sorted(intervals)
        res = intervals[:1]
        for curr_left, curr_right in intervals[1:]:
            if curr_left <= res[-1][1]:
                res[-1][1] = max(curr_right, res[-1][1])
                continue
            res.append([curr_left, curr_right])
        return res


assert_value([[1, 6], [8, 10], [15, 18]], Solution().merge, intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
assert_value([[1, 5]], Solution().merge, intervals=[[1, 4], [4, 5]])
assert_value([[0, 4]], Solution().merge, intervals=[[1, 4], [0, 4]])
assert_value([[0, 4]], Solution().merge, intervals=[[1, 4], [0, 1]])
assert_value([[0, 5]], Solution().merge, intervals=[[1, 4], [0, 2], [3, 5]])
assert_value([[1, 3]], Solution().merge, intervals=[[1, 3]])
assert_value([[1, 4]], Solution().merge, intervals=[[1, 4], [2, 3]])
