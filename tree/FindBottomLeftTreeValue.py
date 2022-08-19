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
