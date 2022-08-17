'''
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = 0
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            res += 1
            for i in range(size):
                curr = curr_level.popleft()
                if not curr.left and not curr.right:
                    return res
                if curr.left:
                    curr_level.append(curr.left)
                if curr.right:
                    curr_level.append(curr.right)

        return res
