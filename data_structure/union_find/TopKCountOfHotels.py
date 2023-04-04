"""
Top K Count Of Hotels
"""
import collections
from typing import List

from test_tool import assert_value


class UnionFind:
    def __init__(self):
        self._cache = {}

    def find(self, hotel_id):
        if hotel_id not in self._cache:
            self._cache[hotel_id] = hotel_id
        while hotel_id != self._cache[hotel_id]:
            hotel_id = self._cache[hotel_id]
        return hotel_id

    def union(self, child, parent):
        root_1 = self.find(child)
        root_2 = self.find(parent)
        if root_1 != root_2:
            self._cache[root_1] = root_2


class Solution:
    def topK(self, scores: List[List[int]], k: int) -> List[List[int]]:
        disjointed_set = UnionFind()
        for child, parent, score in scores:
            disjointed_set.union(child, parent)
        counter = collections.Counter()
        for child, parent, score in scores:
            counter[disjointed_set.find(child)] += score

        return sorted(
            [[hotel_id, score] for hotel_id, score in counter.items()],
            key=lambda item: (-item[1], item[0])
        )[:k]


assert_value([[2, 30], [4, 10]], Solution().topK, scores=[[0, 1, 10], [1, 2, 20], [3, 4, 10], [7, 8, 5]], k=2)
