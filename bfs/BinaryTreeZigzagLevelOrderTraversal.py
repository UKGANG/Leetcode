'''
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''
import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        curr_level = collections.deque([(root, 0)])
        while curr_level:
            next_level = collections.deque([])
            res.append([])
            while curr_level:
                node, n = curr_level.popleft()
                if node.left:
                    next_level.append((node.left, n + 1))
                if node.right:
                    next_level.append((node.right, n + 1))
                if n & 1:
                    res[-1].insert(0, node.val)
                else:
                    res[-1].append(node.val)
            curr_level = next_level
        return res
