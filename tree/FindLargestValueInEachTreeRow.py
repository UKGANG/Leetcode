'''
515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            largest = float('-inf')
            for i in range(size):
                curr = curr_level.popleft()
                largest = max(largest, curr.val)
                if curr.left:
                    curr_level.append(curr.left)
                if curr.right:
                    curr_level.append(curr.right)
            res.append(largest)
        return res
