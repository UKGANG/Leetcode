'''
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
from typing import List, Optional

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = [(root)]
        while q:
            res_level = []
            q = self.level_taverse(q, res_level)
            res.append(res_level)
        return res

    def level_taverse(self, queue: List[TreeNode], res: List[int]) -> List[TreeNode]:
        queue_next = []
        for node in queue:
            res.append(node.val)
            if node.left:
                queue_next.append(node.left)
            if node.right:
                queue_next.append(node.right)

        return queue_next
