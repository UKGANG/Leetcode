'''
652. Find Duplicate Subtrees
https://leetcode.com/problems/find-duplicate-subtrees/
'''
from typing import List, Optional, Tuple

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(root):
            if not root:
                return "-"
            left = dfs(root.left)
            right = dfs(root.right)
            key = f'{root.val}|{left}|{right}'
            if key not in cache:
                cache[key] = 0
            cache[key] += 1
            if cache[key] == 2:
                res.append(root)
            return key

        res = []
        cache = {}
        dfs(root)
        return res
