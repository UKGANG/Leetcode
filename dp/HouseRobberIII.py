'''
337. House Robber III
https://leetcode.com/problems/house-robber-iii/
'''
from typing import List, Optional

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def backtrack(node):
            if not node.left and not node.right:
                return node.val, 0
            val_left, val_no_left = backtrack(node.left) if node.left else (0, 0)
            val_right, val_no_right = backtrack(node.right) if node.right else (0, 0)

            return max(val_left + val_right, sum([node.val, val_no_left, val_no_right])), val_left + val_right

        return max(backtrack(root)) if root else 0

    def _rob(self, root: Optional[TreeNode]) -> int:
        def backtrack(node):
            if not node.left and not node.right:
                return node.val, 0, 0
            val_left, val_left_left, val_left_right = backtrack(node.left) if node.left else (0, 0, 0)
            val_right, val_right_left, val_right_right = backtrack(node.right) if node.right else (0, 0, 0)

            return max(val_left + val_right, sum([node.val, val_left_left, val_left_right, val_right_left,
                                                  val_right_right])), val_left, val_right

        return backtrack(root)[0] if root else 0
