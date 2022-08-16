'''
107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''
import collections
from typing import List, Optional

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = collections.deque()
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            res_curr = []
            for i in range(size):
                curr = curr_level.popleft()
                res_curr.append(curr.val)
                if curr.left:
                    curr_level.append(curr.left)
                if curr.right:
                    curr_level.append(curr.right)
            res.appendleft(res_curr)
        return res
