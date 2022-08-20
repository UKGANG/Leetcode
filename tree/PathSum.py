'''
112. Path Sum
https://leetcode.com/problems/path-sum/
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
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(node, curr_sum):
            if not node.left and not node.right:
                if node.val + curr_sum == targetSum:
                    return True
                return False
            if node.left:
                if backtrack(node.left, curr_sum + node.val):
                    return True
            if node.right:
                if backtrack(node.right, curr_sum + node.val):
                    return True
            return False

        if not root:
            return False
        return backtrack(root, 0)
