'''
590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
'''
import collections
from typing import List, Optional

from test_tool import assert_value


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if not curr.children:
                continue
            for child_node in curr.children:
                stack.append(child_node)
        return res[::-1]
