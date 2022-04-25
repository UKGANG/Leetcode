'''
1610. Maximum Number of Visible Points
https://leetcode.com/problems/maximum-number-of-visible-points/
'''
import math
from collections import defaultdict
from typing import List

from test_tool import assert_value


class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        points = [[x - location[0], y - location[1]] for x, y in points]
        res = sum(1 for x, y in points if x == 0 and y == 0)
        points = [[x, y] for x, y in points if x != 0 or y != 0]
        tan = [math.atan2(x, y) for x, y in points]
        angles = [math.degrees(t) for t in tan]
        angles = sorted(angles)
        angles += [a + 360 for a in angles]

        l, r = 0, 0
        max_cnt = 0
        while l < len(angles):
            while r < len(angles) and angles[r] - angle <= angles[l]:
                r += 1
            max_cnt = max(max_cnt, r - l)
            l += 1
        return max_cnt + res


assert_value(3, Solution().visiblePoints, points=[[2, 1], [2, 2], [3, 3]], angle=90, location=[1, 1])
assert_value(4, Solution().visiblePoints, points=[[2, 1], [2, 2], [3, 4], [1, 1]], angle=90, location=[1, 1])
