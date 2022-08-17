'''
429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
import collections
from typing import List

from test_tool import assert_value


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            res.append([])
            for i in range(size):
                curr = curr_level.popleft()
                res[-1].append(curr.val)
                if not curr.children:
                    continue
                for child_node in curr.children:
                    curr_level.append(child_node)
        return res
