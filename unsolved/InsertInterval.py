'''
57. Insert Interval
https://leetcode.com/problems/insert-interval//
'''
from typing import List

from test_tool import assert_value


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda interval: interval[0])
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])

        return res


assert_value([[1, 5], [6, 9]], Solution().insert, intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
assert_value([[1, 2], [3, 10], [12, 16]], Solution().insert, intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
             newInterval=[4, 8])
assert_value([[5, 7]], Solution().insert, intervals=[], newInterval=[5, 7])
assert_value([[1, 5]], Solution().insert, intervals=[[1, 5]], newInterval=[2, 3])
assert_value([[1, 7]], Solution().insert, intervals=[[1, 5]], newInterval=[2, 7])
assert_value([[1, 5], [6, 8]], Solution().insert, intervals=[[1, 5]], newInterval=[6, 8])
assert_value([[0, 9]], Solution().insert, intervals=[[1, 5], [6, 8]], newInterval=[0, 9])
assert_value([[2, 6], [7, 9], [15, 18]], Solution().insert, intervals=[[2, 6], [7, 9]], newInterval=[15, 18])
assert_value([[2, 10], [11, 13]], Solution().insert, intervals=[[2, 4], [5, 7], [8, 10], [11, 13]], newInterval=[3, 8])
