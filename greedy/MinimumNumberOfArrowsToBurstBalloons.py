'''
452. Minimum Number of Arrows to Burst Balloons
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        i = 1
        l, r = points[0]
        while i < len(points):
            if points[i][0] > r:
                res += 1
                l, r = points[i]
            else:
                r = min(r, points[i][1])
            i += 1

        return res
