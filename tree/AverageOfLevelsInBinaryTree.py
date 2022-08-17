'''
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            total = 0
            for i in range(size):
                curr = curr_level.popleft()
                total += curr.val
                if curr.left:
                    curr_level.append(curr.left)
                if curr.right:
                    curr_level.append(curr.right)
            res.append(total / size)

        return res
