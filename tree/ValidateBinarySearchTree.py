'''
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def traverse(root, res):
            if not root:
                return
            traverse(root.left, res)
            res.append(root.val)
            traverse(root.right, res)

        res = []
        traverse(root, res)
        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True

    def _isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        curr = root
        prev = float('-inf')
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if curr.val > prev:
                    prev = curr.val
                else:
                    return False
                curr = curr.right

        return True
