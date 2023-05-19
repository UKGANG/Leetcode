'''
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''
from typing import List, Optional, Tuple

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return None
            nonlocal res
            res = max(res, root.val)
            left = dfs(root.left)
            right = dfs(root.right)

            if root.left:
                res = max(res, left, left + root.val)
            if root.right:
                res = max(res, right, right + root.val)
            if root.left and root.right:
                res = max(res, left + right + root.val)

            left = 0 if not root.left else left
            right = 0 if not root.right else right
            return max(root.val, root.val + left, root.val + right)

        res = root.val
        dfs(root)
        return res


node2 = TreeNode(2)
node_1 = TreeNode(-1)
node2.left = node_1

assert_value(2, Solution().maxPathSum, root=node2)

node5 = TreeNode(5)
node4_1 = TreeNode(4)
node8 = TreeNode(8)
node11 = TreeNode(11)
node13 = TreeNode(13)
node4_2 = TreeNode(4)
node7 = TreeNode(7)
node2 = TreeNode(2)
node1 = TreeNode(1)

node5.left = node4_1
node5.right = node8

node4_1.left = node11

node8.left = node13
node8.right = node4_2

node11.left = node7
node11.right = node2

node2.left = None
node2.right = None

node4_2.right = node1

assert_value(48, Solution().maxPathSum, root=node5)
