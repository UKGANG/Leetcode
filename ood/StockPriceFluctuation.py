'''
2034. Stock Price Fluctuation
https://leetcode.com/problems/stock-price-fluctuation/
'''
import heapq
from typing import List, Optional, Tuple

from test_tool import assert_value


class StockPrice:

    def __init__(self):
        self._t_price = {}
        self._min_heap = []
        self._max_heap = []
        self._latest = float('-inf')

    def update(self, timestamp: int, price: int) -> None:
        self._t_price[timestamp] = price
        heapq.heappush(self._min_heap, (price, timestamp))
        heapq.heappush(self._max_heap, (-price, timestamp))
        self._latest = max(self._latest, timestamp)

    def current(self) -> int:
        return self._t_price[self._latest]

    def maximum(self) -> int:
        p, t = self._max_heap[0]
        while -p != self._t_price[t]:
            heapq.heappop(self._max_heap)
            p, t = self._max_heap[0]
        return -p

    def minimum(self) -> int:
        p, t = self._min_heap[0]
        while p != self._t_price[t]:
            heapq.heappop(self._min_heap)
            p, t = self._min_heap[0]
        return p

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()