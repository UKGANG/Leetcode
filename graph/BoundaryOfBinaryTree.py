"""
545. Boundary of Binary Tree
https://leetcode.com/problems/boundary-of-binary-tree/description/
"""

# Definition for a binary tree node.
from typing import Optional, List, NoReturn


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def collect_left(node: Optional[TreeNode]) -> NoReturn:
            if not node:
                return
            if node.left or node.right:
                res.append(node.val)
            if node.left:
                collect_left(node.left)
            elif node.right:
                collect_left(node.right)

        def collect_right(node: Optional[TreeNode]) -> NoReturn:
            if not node:
                return
            if node.right:
                collect_right(node.right)
            elif node.left:
                collect_right(node.left)
            if node.left or node.right:
                res.append(node.val)

        def collect_leave(node: Optional[TreeNode]) -> NoReturn:
            if not node:
                return
            if not node.left and not node.right:
                res.append(node.val)
            collect_leave(node.left)
            collect_leave(node.right)

        res = [root.val]
        collect_left(root.left)
        collect_leave(root.left)
        collect_leave(root.right)
        collect_right(root.right)

        return res
