'''
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
'''
from typing import List, Optional

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        return res

    def _preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self._pre_order(root, res)
        return res

    def _pre_order(self, root: Optional[TreeNode], result: List[int]) -> NoReturn:
        if not root:
            return
        result.append(root.val)
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)
