'''
450. Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr and curr.left:
                    curr = curr.left
                curr.val, root.val = root.val, curr.val
                root.right = self.deleteNode(root.right, key)

        return root

    def _deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def backtrack(prev, curr):
            if not curr:
                return
            if curr.val is None or curr.val > key:
                backtrack(curr, curr.left)
            elif curr.val < key:
                backtrack(curr, curr.right)
            else:
                curr_left = curr.left
                curr_right = curr.right
                if not curr_left and not curr_right:
                    new_node = None
                elif not curr_left:
                    new_node = curr_right
                elif not curr_right:
                    new_node = curr_left
                else:
                    new_node = curr_right
                    while curr_right and curr_right.left:
                        curr_right = curr_right.left
                    curr_right.left = curr_left
                if prev.val is None or prev.val > key:
                    prev.left = new_node
                else:
                    prev.right = new_node

        dummy = TreeNode(None)
        dummy.left = root
        backtrack(dummy, root)
        return dummy.left

    def _deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def backtrack(prev, curr):
            if not curr:
                return
            if curr.val is None or curr.val > key:
                backtrack(curr, curr.left)
            elif curr.val < key:
                backtrack(curr, curr.right)
            else:
                curr_left = curr.left
                curr_right = curr.right
                prev_curr_right = None
                while curr_right and curr_right.left:
                    prev_curr_right = curr_right
                    curr_right = curr_right.left
                if prev_curr_right:
                    prev_curr_right.left = curr_right.right
                if curr_right:
                    curr_right.left = curr_left
                if curr_right != curr.right:
                    curr_right.right = curr.right
                new_node = curr_right
                if not new_node:
                    new_node = curr_left
                if prev.val is None or prev.val > key:
                    prev.left = new_node
                else:
                    prev.right = new_node

        dummy = TreeNode(None)
        dummy.left = root
        backtrack(dummy, root)
        return dummy.left
