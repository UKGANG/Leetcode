'''
149. Max Points on a Line
https://leetcode.com/problems/max-points-on-a-line/
'''
from collections import defaultdict
from typing import List

from test_tool import assert_value


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 1

        slope_cache = defaultdict(set)
        for a in range(len(points) - 1):
            for b in range(a + 1, len(points)):
                p1 = tuple(points[a])
                p2 = tuple(points[b])
                slope = float('inf') if p1[0] == p2[0] else (p1[1] - p2[1]) / (p1[0] - p2[0])
                intercept = p1[0] if p1[0] == p2[0] else p1[1] - slope * p1[0]
                slope_cache[(slope, intercept)] |= set([p1, p2])

        return len(sorted(slope_cache.items(), key=lambda item: len(item[1]), reverse=True)[0][1])


assert_value(1, Solution().maxPoints, points=[[0, 0]])
assert_value(3, Solution().maxPoints, points=[[1, 1], [2, 2], [3, 3]])
assert_value(4, Solution().maxPoints, points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]])
assert_value(6, Solution().maxPoints,
             points=[[7, 3], [19, 19], [-16, 3], [13, 17], [-18, 1], [-18, -17], [13, -3], [3, 7], [-11, 12], [7, 19],
                     [19, -12], [20, -18], [-16, -15], [-10, -15], [-16, -18], [-14, -1], [18, 10], [-13, 8], [7, -5],
                     [-4, -9], [-11, 2], [-9, -9], [-5, -16], [10, 14], [-3, 4], [1, -20], [2, 16], [0, 14], [-14, 5],
                     [15, -11], [3, 11], [11, -10], [-1, -7], [16, 7], [1, -11], [-8, -3], [1, -6], [19, 7], [3, 6],
                     [-1, -2], [7, -3], [-6, -8], [7, 1], [-15, 12], [-17, 9], [19, -9], [1, 0], [9, -10], [6, 20],
                     [-12, -4], [-16, -17], [14, 3], [0, -1], [-18, 9], [-15, 15], [-3, -15], [-5, 20], [15, -14],
                     [9, -17], [10, -14], [-7, -11], [14, 9], [1, -1], [15, 12], [-5, -1], [-17, -5], [15, -2],
                     [-12, 11], [19, -18], [8, 7], [-5, -3], [-17, -1], [-18, 13], [15, -3], [4, 18], [-14, -15],
                     [15, 8], [-18, -12], [-15, 19], [-9, 16], [-9, 14], [-12, -14], [-2, -20], [-3, -13], [10, -7],
                     [-2, -10], [9, 10], [-1, 7], [-17, -6], [-15, 20], [5, -17], [6, -6], [-11, -8]])
