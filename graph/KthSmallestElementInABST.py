'''
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
'''
from typing import List, Optional, Tuple

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        curr = root
        while stack:
            while curr:
                if curr.left:
                    stack.append(curr.left)
                curr = curr.left

            curr = stack.pop()
            if k == 1:
                return curr.val
            k -= 1
            if curr.right:
                stack.append(curr.right)
            curr = curr.right
