'''
538. Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/
'''
import collections
from typing import List, Optional, NoReturn

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = 0
        curr = root
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.right
            else:
                curr = stack.pop()
                curr.val += res
                res = curr.val
                curr = curr.left
        return root

    def _convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = 0

        def dfs(curr):
            if not curr:
                return
            nonlocal res
            dfs(curr.right)
            curr.val += res
            res = curr.val
            dfs(curr.left)

        dfs(root)
        return root
