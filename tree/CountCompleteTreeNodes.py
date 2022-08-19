'''
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cnt_left = 0
        curr = root.left
        while curr:
            cnt_left += 1
            curr = curr.left
        cnt_right = 0
        curr = root.right
        while curr:
            cnt_right += 1
            curr = curr.right
        if cnt_left == cnt_right:
            return (2 << cnt_left) - 1
        return self.countNodes(root.left) + self.countNodes(root.right) + 1
