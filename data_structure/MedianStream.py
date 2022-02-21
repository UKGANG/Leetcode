'''
Median Stream
'''
import heapq
from test_tool import assert_value


class MedianHeap:
    def __init__(self):
        self._max_heap = []
        self._min_heap = []

    def push(self, n1):
        if len(self._max_heap) == 0:
            heapq.heappush(self._max_heap, -n1)
            return
        if len(self._min_heap) == 0:
            heapq.heappush(self._min_heap, n1)
            return

        if len(self._max_heap) == len(self._min_heap):
            if n1 >= self._min_heap[0]:
                heapq.heappush(self._min_heap, n1)
            else:
                heapq.heappush(self._max_heap, -n1)
            return

        if len(self._max_heap) > len(self._min_heap):
            n2 = -heapq.heappop(self._max_heap)
        else:
            n2 = heapq.heappop(self._min_heap)
        n = sorted([n1, n2])
        heapq.heappush(self._min_heap, n[1])
        heapq.heappush(self._max_heap, -n[0])

    def peek(self):
        if len(self._max_heap) == len(self._min_heap):
            return (self._min_heap[0] - self._max_heap[0]) >> 1

        if len(self._max_heap) > len(self._min_heap):
            return -self._max_heap[0]

        return self._min_heap[0]


def findMedian(arr):
    res = []
    heap = MedianHeap()
    for i in arr:
        heap.push(i)
        res.append(heap.peek())

    return res


assert_value([5, 10, 5, 4], findMedian, arr=[5, 15, 1, 3])
assert_value([1, 1], findMedian, arr=[1, 2])
