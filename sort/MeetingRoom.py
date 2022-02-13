'''
920 · Meeting Rooms
https://www.lintcode.com/problem/920
'''
import heapq
import random
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def canAttendMeetings(self, intervals: List[Tuple[int]]) -> bool:
        if len(intervals) == 1:
            return True

        intervals = sorted(intervals)
        start_prev, end_prev = intervals[0][0], intervals[0][1]
        for start_curr, end_curr in intervals[1:]:
            if end_prev > start_curr:
                return False

        return True


assert_value(False, Solution().canAttendMeetings, intervals=[[0, 30], [5, 10], [15, 20]])
assert_value(True, Solution().canAttendMeetings, intervals=[[7, 10], [2, 4]])
