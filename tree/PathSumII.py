'''
113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def backtrack(node, curr_sum, curr_list, res):
            if not node.left and not node.right:
                if curr_sum == targetSum and curr_list:
                    res.append(curr_list[:])
                return
            if node.left:
                curr_list.append(node.left.val)
                backtrack(node.left, curr_sum + node.left.val, curr_list, res)
                curr_list.pop()
            if node.right:
                curr_list.append(node.right.val)
                backtrack(node.right, curr_sum + node.right.val, curr_list, res)
                curr_list.pop()

        if not root:
            return [];
        res = []
        backtrack(root, root.val, [root.val], res)
        return res
