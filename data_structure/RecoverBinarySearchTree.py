'''
99. Recover Binary Search Tree
https://leetcode.com/problems/recover-binary-search-tree/
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        curr = root
        stack = []
        left = None
        right = None
        prev = None
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            if stack:
                curr = stack.pop()
                if prev and prev.val > curr.val:
                    if not left:
                        left = prev
                    right = curr
                prev = curr
                curr = curr.right

        # swap
        left.val, right.val = right.val, left.val


s = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n3
n3.right = n2

s.recoverTree(n1)

