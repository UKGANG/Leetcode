'''
530. Minimum Absolute Difference in BST
https://leetcode.com/problems/minimum-absolute-difference-in-bst/
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            global prev, res
            if not root:
                return
            traverse(root.left)
            if prev is not None:
                res = min(res, root.val - prev)
            prev = root.val
            traverse(root.right)

        global prev, res
        prev = None
        res = float('inf')
        traverse(root)

        return res

    def _getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            global nums
            if not root:
                return
            traverse(root.left)
            nums.append(root.val)
            traverse(root.right)

        global nums
        nums = []
        traverse(root)

        res = float('inf')
        for i in range(1, len(nums)):
            res = min(res, nums[i] - nums[i - 1])

        return res

    def __getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        stack = []
        curr = root
        prev = None
        res = float('inf')
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if prev is None:
                    prev = curr.val
                else:
                    res = min(res, curr.val - prev)
                prev = curr.val
                curr = curr.right

        return res
