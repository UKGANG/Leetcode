"""
305. Number of Islands II
https://leetcode.com/problems/number-of-islands-ii/description/
"""
from typing import List


class UnionFindSet:
    def __init__(self):
        self._cache_dict = {}
        self._size = 0

    def create(self, x, y):
        if self.has(x, y):
            return
        self._cache_dict[(x, y)] = (x, y)
        self._size += 1

    def find(self, x, y):
        while self._cache_dict[(x, y)] != (x, y):
            x, y = self._cache_dict[(x, y)]
        return x, y

    def union(self, x1, y1, x2, y2):
        x1_root, y1_root = self.find(x1, y1)
        x2_root, y2_root = self.find(x2, y2)
        if (x1_root, y1_root) == (x2_root, y2_root):
            return
        self._cache_dict[(x1_root, y1_root)] = x2_root, y2_root
        self._size -= 1

    def has(self, x, y):
        return (x, y) in self._cache_dict

    def size(self):
        return self._size


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf_set = UnionFindSet()
        res = []
        for x, y in positions:
            uf_set.create(x, y)
            try:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    _x, _y = x + dx, y + dy
                    if not 0 <= _x < m or not 0 <= _y < n:
                        continue
                    if not uf_set.has(_x, _y):
                        continue
                    uf_set.union(x, y, _x, _y)
            finally:
                res.append(uf_set.size())

        return res
