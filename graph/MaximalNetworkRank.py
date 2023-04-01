"""
1615. Maximal Network Rank
https://leetcode.com/problems/maximal-network-rank
"""
import collections
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for node_0, node_1 in roads:
            graph[node_0].add(node_1)
            graph[node_1].add(node_0)

        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                res = max(res, len(graph[i]) + len(graph[j]) - (1 if j in graph[i] else 0))
        return res
