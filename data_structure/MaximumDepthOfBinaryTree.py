'''
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
from typing import List

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [(root, 1)]
        depth = 1
        while q:
            node, layer = q.pop()
            if node.left:
                q.append((node.left, layer + 1))
            if node.right:
                q.append((node.right, layer + 1))
            depth = max(layer, depth)

        return depth
