"""
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/description/
"""
import operator
from collections import defaultdict
from functools import reduce
from typing import List


class UnionFind:
    def __init__(self):
        self._cache = {}

    def create(self, x):
        self._cache[x] = (x, 1)

    def find(self, x):
        if x not in self._cache:
            return None, -1
        value = 1
        while x != self._cache[x][0]:
            x, value = self._cache[x][0], value * self._cache[x][1]
        return x, value

    def union(self, x, y, value):
        x_root, x_value = self.find(x)
        y_root, y_value = self.find(y)
        if x_root != y_root:
            self._cache[x_root] = (y_root, value * y_value / x_value)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        union_find = UnionFind()
        for node in set(sum(equations, [])):
            union_find.create(node)

        for (x, y), value in zip(equations, values):
            union_find.union(x, y, value)

        res = []
        for x, y in queries:
            x_root, x_value = union_find.find(x)
            y_root, y_value = union_find.find(y)
            value = -1
            if x_root and x_root == y_root:
                value = x_value / y_value
            res.append(value)
        return res

    def _calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def backtrack(a, b):
            if a == b:
                if len(curr):
                    return reduce(operator.mul, curr, 1)
                else:
                    return 1 if a in graph else -1
            for _a, val in graph[a].items():
                if _a in seen:
                    continue
                seen.add(_a)
                curr.append(val)
                val = backtrack(_a, b)
                if val is not None:
                    return val
                curr.pop()
                seen.remove(_a)
            return None

        graph = defaultdict(defaultdict)
        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]
            graph[a][b] = val
            graph[b][a] = 1 / val

        res = []
        curr = []
        seen = set()
        for query in queries:
            seen.clear()
            curr.clear()
            a, b = query
            seen.add(a)
            val = backtrack(a, b)
            if val is None:
                val = -1
            res.append(val)
            seen.remove(a)
        return res
