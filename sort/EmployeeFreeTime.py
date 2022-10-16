'''
759. Employee Free Time
https://leetcode.com/problems/employee-free-time/
'''

# Definition for an Interval.
from itertools import chain


class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        intervals = sorted(chain(*schedule), key=lambda interval: interval.start)
        prev_start, prev_end = intervals[0].start, intervals[0].end
        res = []
        for interval in intervals[1:]:
            curr_start, curr_end = interval.start, interval.end
            if curr_start <= prev_end:
                prev_end = max(prev_end, curr_end)
            else:
                res.append(Interval(prev_end, curr_start))
                prev_start, prev_end = curr_start, curr_end

        return res

    def _employeeFreeTime_tle(self, schedule: '[[Interval]]') -> '[Interval]':
        left = float('inf')
        right = -float('inf')
        for intervals in schedule:
            for interval in intervals:
                left = min(left, interval.start)
                right = max(right, interval.end)

        timeslot = [False] * (right - left)

        for intervals in schedule:
            for interval in intervals:
                timeslot[interval.start - left: interval.end - left] = [True] * (interval.end - interval.start)
        res = []
        l, r = 0, 0
        while l < len(timeslot) and r < len(timeslot):
            while l < len(timeslot) and timeslot[l]:
                l += 1
            r = l + 1
            while r < len(timeslot) and not timeslot[r]:
                r += 1
            if l < len(timeslot):
                res.append(Interval(l + left, r + left))
            l = r + 1
            r = l + 1
        return res
