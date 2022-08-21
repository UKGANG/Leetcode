'''
700. Search in a Binary Search Tree
https://leetcode.com/problems/search-in-a-binary-search-tree/
'''
from typing import List, Optional

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        return None

    def _searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [root]
        curr = root
        while stack:
            while curr:
                if curr.left:
                    stack.append(curr.left)
                curr = curr.left
            if not stack:
                break
            curr = stack.pop()
            if curr.val == val:
                return curr
            if curr.right:
                stack.append(curr.right)
            curr = curr.right
        return None
