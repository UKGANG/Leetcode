'''
Median Heap
'''
import heapq
import random
from typing import List

from test_tool import assert_value


class MedianHeap:
    def __init__(self):
        self._max_heap = []
        self._min_heap = []

    def size(self):
        return len(self._min_heap) + len(self._max_heap)

    def peek(self):
        if len(self._min_heap) > len(self._max_heap):
            return self._min_heap[0]
        else:
            return -self._max_heap[0]

    def push(self, val: int):
        if not len(self._max_heap):
            heapq.heappush(self._max_heap, -val)

        if len(self._max_heap) >= len(self._min_heap):
            if self._max_heap[0] < -val:
                heapq.heappush(self._min_heap, -self._max_heap[0])
                heapq.heappop(self._max_heap)
                heapq.heappush(self._max_heap, -val)
            else:
                heapq.heappush(self._min_heap, val)
        else:
            if self._min_heap[0] < val:
                heapq.heappush(self._max_heap, -self._min_heap[0])
                heapq.heappop(self._min_heap)
                heapq.heappush(self._min_heap, val)
            else:
                heapq.heappush(self._max_heap, -val)

    def pop(self):
        if len(self._max_heap) == len(self._min_heap):
            if self._max_heap[0] <= self._min_heap[0]:
                return -heapq.heappop(self._max_heap)
            return heapq.heappop(self._min_heap)
        if len(self._max_heap) > len(self._min_heap):
            return -heapq.heappop(self._max_heap)
        return heapq.heappop(self._min_heap)

    def heapify(self):
        ...

    def get_heap(self):
        return self._heap


heap = MedianHeap()
random_nums = list(range(100))
random.shuffle(random_nums)
for num in random_nums:
    heap.push(num)

for i in reversed(range(len(random_nums) + 1)):
    print(heap.pop())
