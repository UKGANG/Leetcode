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
        stack = [root]
        curr = root
        prev = None
        low, high = None, None
        while stack:
            while curr:
                if curr.left:
                    stack.append(curr.left)
                curr = curr.left
            curr = stack.pop()

            if prev and prev.val > curr.val:
                if not low:
                    low = prev
                high = curr
            prev = curr

            if curr.right:
                stack.append(curr.right)
            curr = curr.right

        low.val, high.val = high.val, low.val


s = Solution()

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.left = n3
n3.right = n2

s.recoverTree(n1)

