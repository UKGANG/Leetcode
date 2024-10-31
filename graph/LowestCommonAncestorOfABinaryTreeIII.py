'''
1650. Lowest Common Ancestor of a Binary Tree III
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
'''

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
        reversed_idx = set()
        while p:
            reversed_idx.add(p)
            p = p.parent
        while q not in reversed_idx:
            reversed_idx.add(q)
            q = q.parent
        return q

    def _lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        node_list = {}
        while p:
            node_list[p.val] = p
            p = p.parent
        while q:
            if q.val in node_list:
                return q
            q = q.parent

        return None
