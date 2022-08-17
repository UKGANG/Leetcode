'''
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        stack = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr.left, curr.right = curr.right, curr.left
                curr = curr.left
        return root

    def _invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        while stack:
            curr = stack.pop()
            if not curr:
                continue
            curr.left, curr.right = curr.right, curr.left
            stack.append(curr.left)
            stack.append(curr.right)
        return root

    def __invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            for i in range(size):
                curr = curr_level.popleft()
                curr.left, curr.right = curr.right, curr.left
                if curr.left:
                    curr_level.append(curr.left)
                if curr.right:
                    curr_level.append(curr.right)
        return root
