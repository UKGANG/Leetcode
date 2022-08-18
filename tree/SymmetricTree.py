'''
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/
'''
import collections
from typing import List, Optional

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]) -> bool:
        if not left_node and not right_node:
            return True
        if not left_node:
            return False
        if not right_node:
            return False
        if left_node.val != right_node.val:
            return False
        left_check = self.compare(left_node.left, right_node.right)
        right_check = self.compare(left_node.right, right_node.left)
        return left_check and right_check

    def _isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        curr_level = collections.deque([root.left, root.right])
        while curr_level:
            next_level = collections.deque()
            while curr_level:
                node_left, node_right = curr_level.popleft(), curr_level.pop()
                if not node_left and not node_right:
                    continue
                if not node_left and node_right:
                    return False
                if node_left and not node_right:
                    return False
                if node_left.val != node_right.val:
                    return False
                next_level.append(node_right.left)
                next_level.appendleft(node_left.right)
                next_level.append(node_right.right)
                next_level.appendleft(node_left.left)
            curr_level = next_level
        return True
