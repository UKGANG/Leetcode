'''
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''
from typing import List

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root

        return left if left else right


    def _lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p = self.findPath(root, p)
        path_q = self.findPath(root, q)
        l, r = 0, min(len(path_p), len(path_q)) - 1

        if path_p[r] == path_q[r]:
            return path_p[r]

        while l < r:
            m = (l + r) >> 1
            if path_p[m].val == path_q[m].val:
                l = m + 1
            else:
                r = m

        return path_p[r - 1]

    def findPath(self, root: 'TreeNode', node: 'TreeNode'):
        if root.val == node.val:
            return [root]
        if root.left:
            path_left = self.findPath(root.left, node)
            if path_left:
                path_left.insert(0, root)
                return path_left
        if root.right:
            path_right = self.findPath(root.right, node)
            if path_right:
                path_right.insert(0, root)
                return path_right
        return None
