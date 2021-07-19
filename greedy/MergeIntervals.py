'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals)
        res, l, r = [], 0, 1
        while l <= r < len(intervals):
            right_bound = intervals[l][1]
            while right_bound >= intervals[r][0]:
                r += 1
                if r == len(intervals):
                    right_bound = max(right_bound, intervals[-1][1])
                    break
                right_bound = max(right_bound, intervals[r - 1][1])
            res.append([intervals[l][0], right_bound])
            l = r

        return res


assert_value([[1, 6], [8, 10], [15, 18]], Solution().merge, intervals=[[1, 3], [2, 6], [8, 10], [15, 18]])
assert_value([[1, 5]], Solution().merge, intervals=[[1, 4], [4, 5]])
assert_value([[0, 4]], Solution().merge, intervals=[[1, 4], [0, 4]])
assert_value([[0, 4]], Solution().merge, intervals=[[1, 4], [0, 1]])
assert_value([[0, 5]], Solution().merge, intervals=[[1, 4], [0, 2], [3, 5]])
assert_value([[1, 3]], Solution().merge, intervals=[[1, 3]])
assert_value([[1, 4]], Solution().merge, intervals=[[1, 4], [2, 3]])
