'''
1135. Connecting Cities With Minimum Cost
https://leetcode.com/problems/connecting-cities-with-minimum-cost/
'''
from operator import itemgetter
from typing import List, NoReturn


class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        def create(i: int) -> NoReturn:
            cache[i] = i

        def find(i: int) -> bool:
            while i != cache[i]:
                i = cache[i]
            return i

        def union(x: int, y: int) -> NoReturn:
            x_root = find(x)
            y_root = find(y)
            if x_root != y_root:
                cache[y_root] = x_root

        cache = {}

        for i in range(n):
            create(i + 1)

        connections.sort(key=itemgetter(2))

        res = 0

        for x, y, dist in connections:
            x_root = find(x)
            y_root = find(y)
            if x_root == y_root:
                continue
            res += dist
            n -= 1
            union(x, y)

        return res if n == 1 else -1

