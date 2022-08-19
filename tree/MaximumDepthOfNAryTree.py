'''
559. Maximum Depth of N-ary Tree
https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
'''
import collections
from typing import List, Optional

from test_tool import assert_value


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        res = 0
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            res += 1
            for i in range(size):
                curr = curr_level.popleft()
                curr_level.extend(curr.children)
        return res
