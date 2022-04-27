'''
2013. Detect Squares
https://leetcode.com/problems/detect-squares/
'''
from collections import Counter
from typing import List

from test_tool import assert_value


class DetectSquares:

    def __init__(self):
        self._x_y_cnt = Counter()

    def add(self, point: List[int]) -> None:
        self._x_y_cnt[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        i, j = point
        res = 0
        for (x, y), cnt in self._x_y_cnt.items():
            if x == i or y == j:
                continue
            if abs(x - i) != abs(y - j):
                continue
            cnt *= self._x_y_cnt[(x, j)]
            cnt *= self._x_y_cnt[(i, y)]
            res += cnt
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)