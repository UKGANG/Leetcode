'''
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree
'''
import heapq
from typing import List, Optional

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max = 0
        self.max_path(root)
        return self.max

    def max_path(self, node):
        if not node:
            return 0
        left = self.max_path(node.left)
        right = self.max_path(node.right)
        self.max = max(left + right, self.max)
        return max(left, right) + 1
