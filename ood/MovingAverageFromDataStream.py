'''
346. Moving Average from Data Stream
https://leetcode.com/problems/moving-average-from-data-stream/
'''
import collections
from typing import List

from test_tool import assert_value


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = collections.deque()
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.sum -= self.q.popleft()
        self.q.append(val)
        self.sum += val
        return self.sum / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)