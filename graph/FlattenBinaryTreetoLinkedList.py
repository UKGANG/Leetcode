'''
114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
'''
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        prev = None
        while stack:
            curr = stack.pop()
            left = curr.left
            right = curr.right
            curr.left = None
            if prev:
                prev.right = curr
            prev = curr
            if right:
                stack.append(right)
            if left:
                stack.append(left)


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node1.left = node2
node1.right = node5

node2.left = node3
node2.right = node4

node5.right = node6

Solution().flatten(node1)

print()
