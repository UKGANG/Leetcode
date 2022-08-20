'''
113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
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
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(node, curr_sum, curr_list, res):
            if not node.left and not node.right:
                if node.val + curr_sum == targetSum:
                    curr_list = curr_list.copy()
                    curr_list.append(node.val)
                    res.append(curr_list)
                    return
                return
            if node.left:
                curr_list.append(node.val)
                backtrack(node.left, curr_sum + node.val, curr_list, res)
                curr_list.pop()
            if node.right:
                curr_list.append(node.val)
                backtrack(node.right, curr_sum + node.val, curr_list, res)
                curr_list.pop()

        if not root:
            return []
        res = []
        backtrack(root, 0, [], res)
        return res
