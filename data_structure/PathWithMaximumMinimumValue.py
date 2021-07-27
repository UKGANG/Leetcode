'''
1102. Path With Maximum Minimum Value
https://leetcode.com/problems/path-with-maximum-minimum-value/
'''
from heapq import heappop, heappush
from typing import List

from test_tool import assert_value


class Solution:
    def maxMinVal(self, points: List[List[int]]) -> int:
        h = [(-points[0][0], 0, 0)]
        visited = set()
        res = -points[0][0]
        while h:
            path, x, y = heappop(h)
            visited.add((x, y))
            res = max(res, path)
            if x == len(points) - 1 and y == len(points[0]) - 1:
                break
            for i, j in {
                (max(0, x - 1), y),
                (x, max(0, y - 1)),
                (min(len(points) - 1, x + 1), y),
                (x, min(len(points[0]) - 1, y + 1)),
            }:
                if (i, j) not in visited:
                    try:
                        heappush(h, (-points[i][j], i, j))
                    except IndexError as e:
                        print(e)

        return -res


assert_value(4, Solution().maxMinVal,
             points=[[5, 4, 5],
                     [1, 2, 6],
                     [7, 4, 6]])
assert_value(2, Solution().maxMinVal,
             points=[[2, 2, 1, 2, 2, 2],
                     [1, 2, 2, 2, 1, 2]])
assert_value(3, Solution().maxMinVal,
             points=[[3, 4, 6, 3, 4],
                     [0, 2, 1, 1, 7],
                     [8, 8, 3, 2, 7],
                     [3, 2, 4, 9, 8],
                     [4, 1, 2, 0, 0],
                     [4, 6, 5, 4, 3]])
