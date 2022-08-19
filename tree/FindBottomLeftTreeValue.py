'''
513. Find Bottom Left Tree Value
https://leetcode.com/problems/find-bottom-left-tree-value/
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
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        global max_val
        global max_depth
        max_val = root.val
        max_depth = 0

        def backtrack(node, depth):
            global max_val
            global max_depth
            if not node.left and not node.right:
                if depth > max_depth:
                    max_val, max_depth = node.val, depth
                return
            if node.left:
                backtrack(node.left, depth + 1)
            if node.right:
                backtrack(node.right, depth + 1)

        backtrack(root, 0)
        return max_val

    def _findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = None
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            for i in range(size):
                curr = curr_level.popleft()
                if not i:
                    res = curr.val
                if curr.left:
                    curr_level.append(curr.left)
                if curr.right:
                    curr_level.append(curr.right)

        return res
