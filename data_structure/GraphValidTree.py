'''
261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/
'''
from collections import defaultdict
from typing import List

from test_tool import assert_value


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """

    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        g = defaultdict(list)
        for s, t in edges:
            g[s].append(t)
            g[t].append(s)

        q = [0]
        visited = [0]
        while q:
            node = q.pop()
            nodes = g[node]
            for _n in nodes:
                if _n in visited:
                    continue
                q.append(_n)
                visited.append(_n)
        return len(visited) == n


assert_value(True, Solution().validTree, n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]])
assert_value(False, Solution().validTree, n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
