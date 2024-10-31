"""
314. Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal
"""
from collections import defaultdict
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = defaultdict(list)
        level = 0
        prev = [(level, root)]
        while prev:
            curr = []
            for level, node in prev:
                res[level].append(node.val)
                if node.left:
                    curr.append((level - 1, node.left))
                if node.right:
                    curr.append((level + 1, node.right))
            prev = curr
        return [res[i] for i in sorted(res.keys())]
