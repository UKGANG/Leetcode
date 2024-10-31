"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list
"""
from typing import List, Tuple

from test_tool import assert_value

"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        head, tail = self.convert(root)
        head.left = tail
        tail.right = head
        return head

    def convert(self, root: 'Optional[Node]') -> Tuple['Optional[Node]', 'Optional[Node]']:
        if not root:
            return None, None
        left_head, left_tail = self.convert(root.left)
        right_head, right_tail = self.convert(root.right)
        root.left = left_tail
        root.right = right_head
        if root.left:
            left_tail.right = root
        if root.right:
            right_head.left = root
        left_head = left_head or root
        right_tail = right_tail or root
        return left_head, right_tail

    def _treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        curr = root
        dummy = Node(None)
        head = dummy
        stack = [root]
        while True:
            while curr:
                if curr.left:
                    stack.append(curr.left)
                curr = curr.left
            curr = stack.pop()
            head.right = curr
            curr.left = head
            head = curr
            if curr.right:
                stack.append(curr.right)
            if not stack:
                curr.right = dummy.right
                dummy.right.left = curr
                break
            curr = curr.right
        return dummy.right
