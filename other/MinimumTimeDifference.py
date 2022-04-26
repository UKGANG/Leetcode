'''
539. Minimum Time Difference
https://leetcode.com/problems/minimum-time-difference/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [self.convert_to_min(ts) for ts in timePoints]
        minutes = sorted(minutes)
        minutes += [m + 24 * 60 for m in minutes]
        diff = []
        for i in range(1, len(minutes)):
            diff.append(minutes[i] - minutes[i - 1])
        return min(diff)

    def convert_to_min(self, ts):
        h, m = ts.split(':')
        return 60 * int(h) + int(m)


assert_value(1, Solution().findMinDifference, timePoints=["23:59", "00:00"])
assert_value(0, Solution().findMinDifference, timePoints=["00:00", "23:59", "00:00"])
