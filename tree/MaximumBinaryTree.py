'''
654. Maximum Binary Tree
https://leetcode.com/problems/maximum-binary-tree/
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
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for n in nums:
            curr = TreeNode(n)
            while stack and stack[-1].val < curr.val:
                curr.left = stack.pop()
            if stack:
                stack[-1].right = curr
            stack.append(curr)
        return stack[0]

    def _constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def backtrack(start, end):
            if start == end:
                return None
            mid = start
            max_val = float('-inf')
            for i in range(start, end):
                if nums[i] > max_val:
                    max_val = nums[i]
                    mid = i
            res = TreeNode(max_val)
            res.left = backtrack(start, mid)
            res.right = backtrack(mid + 1, end)
            return res

        return backtrack(0, len(nums))
