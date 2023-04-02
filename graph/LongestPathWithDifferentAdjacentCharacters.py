"""
2246. Longest Path With Different Adjacent Characters
https://leetcode.com/problems/longest-path-with-different-adjacent-characters
"""
import collections
import heapq
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(parent_node):
            nonlocal res
            trailingLengths = [0]
            for child_node in graph[parent_node]:
                if s[child_node] == s[parent_node]:
                    dfs(child_node)
                else:
                    heapq.heappush(trailingLengths, dfs(child_node))
                    if len(trailingLengths) == 3:
                        heapq.heappop(trailingLengths)
            res = max(res, sum(trailingLengths) + 1)
            return max(trailingLengths) + 1

        graph = collections.defaultdict(set)
        for child_node in range(len(parent)):
            parent_node = parent[child_node]
            graph[parent_node].add(child_node)

        res = 1
        dfs(0)
        return res
