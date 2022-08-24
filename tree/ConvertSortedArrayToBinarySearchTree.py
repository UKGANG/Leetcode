'''
108. Convert Sorted Array to Binary Search Tree
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
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
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        res = TreeNode(None)
        stack = [(res, 0, len(nums))]
        while stack:
            prev, l, r = stack.pop()
            m = (l + r) >> 1
            curr = TreeNode(nums[m])
            if prev.val is None or prev.val > curr.val:
                prev.left = curr
            else:
                prev.right = curr
            if l == m:
                continue
            else:
                stack.append((curr, l, m))
            if r == m + 1:
                continue
            else:
                stack.append((curr, m + 1, r))
        return res.left

    def _sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def backtrack(nums, l, r):
            if l == r:
                return None
            m = (l + r) >> 1
            res = TreeNode(nums[m])
            res.left = backtrack(nums, l, m)
            res.right = backtrack(nums, m + 1, r)
            return res

        return backtrack(nums, 0, len(nums))
