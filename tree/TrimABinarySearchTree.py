'''
669. Trim a Binary Search Tree
https://leetcode.com/problems/trim-a-binary-search-tree/
'''
import collections
from typing import List, Optional, NoReturn

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root:
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
            else:
                break

        if not root:
            return root

        curr = root
        while curr:
            while curr.left and curr.left.val < low:
                curr.left = curr.left.right
            curr = curr.left

        curr = root
        while curr:
            while curr.right and curr.right.val > high:
                curr.right = curr.right.left
            curr = curr.right

        return root

    def _trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val < low:
            return self._trimBST(root.right, low, high)
        if root.val > high:
            return self._trimBST(root.left, low, high)
        root.left = self._trimBST(root.left, low, high)
        root.right = self._trimBST(root.right, low, high)
        return root
