'''
352. Data Stream as Disjoint Intervals
https://leetcode.com/problems/data-stream-as-disjoint-intervals/
'''
import heapq
from typing import List
from collections import defaultdict

from test_tool import assert_value


class SummaryRanges:

    def __init__(self):
        self._interval = []

    def addNum(self, val: int) -> None:
        heapq.heappush(self._interval, (val, [val, val]))

    def getIntervals(self) -> List[List[int]]:
        res = []
        while self._interval:
            curr_start, prev = heapq.heappop(self._interval)
            curr_start, curr_end = prev[0], prev[1]
            if not res:
                res.append((curr_start, [curr_start, curr_end]))
                continue
            prev = res[-1][-1]
            prev_start, prev_end = prev[0], prev[1]
            if prev_end + 1 >= curr_start:
                prev[1] = max(curr_end, prev_end)
                continue
            res.append((curr_start, [curr_start, curr_end]))

        self._interval = res
        return list(map(lambda x: x[1], res))


# Your SummaryRanges object will be instantiated and called as such:
obj = SummaryRanges()
obj.addNum(11)
assert_value([[11, 11]], obj.getIntervals)

obj.addNum(13)
assert_value([[11, 11], [13, 13]], obj.getIntervals)

obj.addNum(17)
assert_value([[11, 11], [13, 13], [17, 17]], obj.getIntervals)

obj.addNum(12)
assert_value([[11, 13], [17, 17]], obj.getIntervals)

obj.addNum(16)
assert_value([[11, 13], [16, 17]], obj.getIntervals)

obj.addNum(1)
assert_value([[1, 1], [11, 13], [16, 17]], obj.getIntervals)

obj.addNum(1)
assert_value([[1, 1], [11, 13], [16, 17]], obj.getIntervals)
