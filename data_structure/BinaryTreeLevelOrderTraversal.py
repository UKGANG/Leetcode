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
        q = [root]
        res = []
        while q:
            curr = []
            q_next = []
            for node in q:
                if not node:
                    continue
                curr.append(node.val)
                if node.left:
                    q_next.append(node.left)
                if node.right:
                    q_next.append(node.right)
            if curr:
                res.append(curr)
            q = q_next
        return res
