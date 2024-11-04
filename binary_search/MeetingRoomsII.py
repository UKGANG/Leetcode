'''
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/
'''
import bisect
import heapq
import operator
from typing import List

from test_tool import assert_value


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = map(operator.itemgetter(0), intervals)
        ends = map(operator.itemgetter(1), intervals)
        starts = sorted(starts)
        ends = sorted(ends)

        res = 0
        end_idx = 0
        for start_idx in range(len(starts)):
            if starts[start_idx] < ends[end_idx]:
                res += 1
            else:
                end_idx += 1

        return res

    def minMeetingRooms_v1(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)

        available_ending_time = []
        for start, end in intervals:
            if available_ending_time and available_ending_time[0] <= start:
                heapq.heappop(available_ending_time)
            heapq.heappush(available_ending_time, end)
        return len(available_ending_time)

    def minMeetingRooms_v0(self, intervals: List[List[int]]) -> int:
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
