'''
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/
'''
from heapq import heappop, heappush
from typing import List

from test_tool import assert_value


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for idx, (x, y) in enumerate(points):
            dist = -x ** 2 - y ** 2
            if len(res) == k:
                if res[0][0] <= dist:
                    heappop(res)
                else:
                    continue
            heappush(res, (dist, idx, x, y))
        return [[x, y] for rank, idx, x, y in sorted(res, key=lambda item: item[1])]


assert_value([[-2, 2]], Solution().kClosest, points=[[1, 3], [-2, 2]], k=1)
assert_value([[3, 3], [-2, 4]], Solution().kClosest, points=[[3, 3], [5, -1], [-2, 4]], k=2)
assert_value([[1, 1]], Solution().kClosest, points=[[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]], k=1)
assert_value([[2, 31], [-27, -38], [-55, -39], [-57, -67], [34, -84]], Solution().kClosest,
             points=[[68, 97], [34, -84], [60, 100], [2, 31], [-27, -38], [-73, -74], [-55, -39], [62, 91], [62, 92],
                     [-57, -67]], k=5)
