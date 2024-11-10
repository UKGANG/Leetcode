"""
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value
"""
from collections import deque
from typing import List, Optional

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        queue = deque([root])
        res = float('inf')
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.val == target:
                    return node.val
                abs_res = abs(target - res)
                abs_node = abs(target - node.val)
                if abs_res > abs_node:
                    res = node.val
                elif abs_res == abs_node:
                    res = min(res, node.val)
                if node.val > target:
                    if node.left:
                        queue.append(node.left)
                else:
                    if node.right:
                        queue.append(node.right)
        return res
