'''
1584. Min Cost to Connect All Points
https://leetcode.com/problems/min-cost-to-connect-all-points/
'''
import heapq
from typing import List

from test_tool import assert_value


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d, res = {(x, y): float('inf') if i else 0 for i, (x, y) in enumerate(points)}, 0
        while d:
            x, y = min(d, key=d.get)  # obtain the current minimum edge
            res += d.pop((x, y))  # and remove the corresponding point
            for x1, y1 in d:  # for the rest of the points, update the minimum manhattan distance
                d[(x1, y1)] = min(d[(x1, y1)], abs(x - x1) + abs(y - y1))
        return res


assert_value(20, Solution().minCostConnectPoints, points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]])
assert_value(18, Solution().minCostConnectPoints, points=[[3, 12], [-2, 5], [-4, 1]])
