'''
919 · Meeting Rooms II
https://www.lintcode.com/problem/920
'''
import heapq
import random
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def minMeetingRooms(self, intervals: List[Tuple[int]]) -> int:
        cnt = []
        for s, e in intervals:
            heapq.heappush(cnt, (s, 'start'))
            heapq.heappush(cnt, (e, 'end'))
        res, curr = 0, 0
        while cnt:
            t, i = heapq.heappop(cnt)
            if i == 'start':
                curr += 1
            else:
                curr -= 1
            res = max(curr, res)
        return res


assert_value(2, Solution().minMeetingRooms, intervals=[(0, 30), (5, 10), (15, 20)])
assert_value(1, Solution().minMeetingRooms, intervals=[(2, 7)])
