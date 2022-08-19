'''
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
'''
import collections
from typing import List, Optional

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.get_height(root) != -1

    def get_height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.get_height(root.left)
        if -1 == left_height:
            return -1
        right_height = self.get_height(root.right)
        if -1 == right_height:
            return -1
        if abs(right_height - left_height) > 1:
            return -1
        return max(left_height, right_height) + 1
