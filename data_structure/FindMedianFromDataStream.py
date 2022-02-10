'''
295. Find Median from Data Stream
https://leetcode.com/problems/find-median-from-data-stream/
'''
import heapq
from typing import List

from test_tool import assert_value


class MedianFinder:

    def __init__(self):
        self._max_heap = []
        self._min_heap = []

    def addNum(self, num: int) -> None:
        if not self._max_heap and not self._min_heap:
            heapq.heappush(self._max_heap, -num)
            return
        if len(self._max_heap) >= len(self._min_heap):
            if self._max_heap[0] < -num:
                heapq.heappush(self._min_heap, -self._max_heap[0])
                heapq.heappop(self._max_heap)
                heapq.heappush(self._max_heap, -num)
            else:
                heapq.heappush(self._min_heap, num)
        else:
            if self._min_heap[0] < num:
                heapq.heappush(self._max_heap, -self._min_heap[0])
                heapq.heappop(self._min_heap)
                heapq.heappush(self._min_heap, num)
            else:
                heapq.heappush(self._max_heap, -num)

    def findMedian(self) -> float:
        if len(self._max_heap) == len(self._min_heap):
            return (self._min_heap[0] - self._max_heap[0]) / 2
        if len(self._max_heap) >= len(self._min_heap):
            return -self._max_heap[0]
        return self._min_heap[0]


heap = MedianFinder()

heap.addNum(1)
heap.addNum(2)
assert_value(1.5, heap.findMedian)

heap.addNum(3)
assert_value(2, heap.findMedian)
