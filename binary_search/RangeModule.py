'''
715. Range Module
https://leetcode.com/problems/range-module/
'''
import bisect
from typing import List

from test_tool import assert_value


class RangeModule:

    def __init__(self):
        self._range = []

    def addRange(self, left: int, right: int) -> None:
        idx_left = bisect.bisect_left(self._range, left)
        idx_right = bisect.bisect_right(self._range, right)

        new_range = []
        if idx_left & 1 == 0:
            new_range.append(left)
        if idx_right & 1 == 0:
            new_range.append(right)

        self._range[idx_left:idx_right] = new_range

    def queryRange(self, left: int, right: int) -> bool:
        idx_left = bisect.bisect_right(self._range, left)
        idx_right = bisect.bisect_left(self._range, right)

        return idx_left == idx_right and idx_left & 1

    def removeRange(self, left: int, right: int) -> None:
        idx_left = bisect.bisect_left(self._range, left)
        idx_right = bisect.bisect_right(self._range, right)

        new_range = []
        if idx_left & 1:
            new_range.append(left)
        if idx_right & 1:
            new_range.append(right)

        self._range[idx_left:idx_right] = new_range


# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10, 20)
obj.removeRange(14, 16)
param_2 = obj.queryRange(10, 14)
param_3 = obj.queryRange(13, 15)
param_4 = obj.queryRange(16, 17)
