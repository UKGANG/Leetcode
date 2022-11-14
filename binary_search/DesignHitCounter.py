'''
362. Design Hit Counter
https://leetcode.com/problems/design-hit-counter/
'''
from typing import List

from test_tool import assert_value


class HitCounter:
    def __init__(self):
        self._hits = []

    def hit(self, timestamp: int) -> None:
        self._hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        left = self._search(timestamp - 300)
        right = self._search(timestamp)
        return right - left

    def _search(self, timestamp: int) -> int:
        l, r = 0, len(self._hits)
        while l < r:
            m = l + ((r - l) >> 1)
            if self._hits[m] <= timestamp:
                l = m + 1
            else:
                r = m
        return r
