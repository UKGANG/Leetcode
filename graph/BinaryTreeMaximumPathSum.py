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
        cache = {}
        self.dfs(root, cache)
        return cache['res']

    def dfs(self, root: Optional[TreeNode], cache) -> int:
        if not root:
            return None
        left = self.dfs(root.left, cache)
        right = self.dfs(root.right, cache)
        max_val = cache.get('res', root.val)
        if left:
            max_val = max(max_val, left, left + root.val)
        if right:
            max_val = max(max_val, right, right + root.val)
        if left and right:
            max_val = max(max_val, left + right + root.val)
        max_val = max(max_val, root.val)
        cache['res'] = max_val

        left = 0 if not left else left
        right = 0 if not right else right
        return max(root.val, root.val + left, root.val + right)


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
