"""
285. Inorder Successor in BST
https://leetcode.com/problems/inorder-successor-in-bst
"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        stack = []
        curr = root
        found = False
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if found:
                return curr
            if curr.val == p.val:
                found = True
            curr = curr.right
        return None
