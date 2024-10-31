"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/
"""
from typing import List, Optional

from test_tool import assert_value

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        cache = {}
        return self.copy(node, cache)

    def copy(self, node, cache):
        copied_node = Node(node.val)
        cache[node.val] = copied_node
        neighbors = []
        for neighbor in node.neighbors:
            if neighbor.val not in cache:
                self.copy(neighbor, cache)
            neighbors.append(cache[neighbor.val])
        copied_node.neighbors = neighbors
        return copied_node
