'''
939. Minimum Area Rectangle

'''
from typing import List, Optional

from test_tool import assert_value


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:

        def calculate_square(a, b):
            res_inner = float('inf')
            for c, d in points:
                if (c > a and d > b) and (a, d) in cache and (c, b) in cache:
                    res_inner = min(res, abs((c - a) * (d - b)))
                    break
            return res_inner

        points = sorted(points, key=lambda point: point[0] ** 2 + point[1] ** 2)

        cache = set()
        for point in points:
            cache.add((point[0], point[1]))

        res = float('inf')
        for point in points:
            square = calculate_square(*point)
            res = min(res, square)

        return 0 if res == float('inf') else res


assert_value(4, Solution().minAreaRect, points=[[1, 1], [1, 3], [3, 1], [3, 3], [2, 2]])
assert_value(2, Solution().minAreaRect, points=[[1, 1], [1, 3], [3, 1], [3, 3], [4, 1], [4, 3]])
