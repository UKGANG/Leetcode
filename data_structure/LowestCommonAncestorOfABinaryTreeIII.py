'''
1650. Lowest Common Ancestor of a Binary Tree III
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
'''
from collections import defaultdict
from typing import List

from test_tool import assert_value

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        node_list = {}
        while p:
            node_list[p.val] = p
            p = p.parent
        while q:
            if q.val in node_list:
                return q
            q = q.parent

        return None
