'''
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/
'''
import bisect
from typing import List

from test_tool import assert_value


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals)
        res = 1
        endings = []
        for start, end in intervals:
            idx = bisect.bisect_right(endings, start)
            curr = len(endings) - idx
            res = max(res, curr + 1)
            endings = endings[idx:]
            bisect.insort_left(endings, end)

        return res


assert_value(2, Solution().minMeetingRooms, intervals=[[0, 30], [5, 10], [15, 20]])
assert_value(1, Solution().minMeetingRooms, intervals=[[7, 10], [2, 4]])
assert_value(1, Solution().minMeetingRooms, intervals=[[13, 15], [1, 13]])
