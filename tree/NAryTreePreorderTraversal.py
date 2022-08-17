'''
589. N-ary Tree Preorder Traversal
https://leetcode.com/problems/n-ary-tree-preorder-traversal/
'''
import collections
from typing import List, Optional

from test_tool import assert_value


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if not curr.children:
                continue
            for child_node in reversed(curr.children):
                stack.append(child_node)

        return res
