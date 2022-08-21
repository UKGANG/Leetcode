'''
617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/
'''
import collections
from typing import List, Optional, NoReturn

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        dummy_node = TreeNode()
        curr_level = collections.deque([(dummy_node, True, root1, root2)])
        while curr_level:
            parent, is_left, node1, node2 = curr_level.popleft()
            if not node1:
                new_node = node2
            elif not node2:
                new_node = node1
            else:
                new_node = node1
                new_node.val += node2.val
            if is_left:
                parent.left = new_node
            else:
                parent.right = new_node

            node1_left = node1.left if node1 else None
            node2_left = node2.left if node2 else None
            node1_right = node1.right if node1 else None
            node2_right = node2.right if node2 else None

            if node1_left or node2_left:
                curr_level.append((new_node, True, node1_left, node2_left))
            if node1_right or node2_right:
                curr_level.append((new_node, False, node1_right, node2_right))
        return dummy_node.left

    def _mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
