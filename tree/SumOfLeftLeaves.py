'''
404. Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        stack = []
        curr = (root, False)
        while curr[0] or stack:
            if curr[0]:
                stack.append(curr)
                curr = (curr[0].left, True)
            else:
                curr = stack.pop()
                if curr[1] and not curr[0].left and not curr[0].right:
                    res += curr[0].val
                curr = (curr[0].right, False)
        return res

    def _sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self._sum_left(root, False)

    def _sum_left(self, root: Optional[TreeNode], is_left: bool) -> int:
        if not root:
            return 0
        if is_left and not root.left and not root.right:
            return root.val
        left_sum = self.sum_left(root.left, True)
        right_sum = self.sum_left(root.right, False)
        return left_sum + right_sum
