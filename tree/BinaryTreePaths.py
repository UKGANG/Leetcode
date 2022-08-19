'''
257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
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
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        curr_prefix = []
        res = []
        self.get_all_paths(root, curr_prefix, res)
        return res

    def get_all_paths(self, curr: Optional[TreeNode], curr_prefix: List[int], res: List[List[int]]) -> NoReturn:
        curr_prefix.append(str(curr.val))
        if curr.left:
            self.get_all_paths(curr.left, curr_prefix.copy(), res)
        if curr.right:
            self.get_all_paths(curr.right, curr_prefix.copy(), res)
        if not curr.left and not curr.right:
            res.append('->'.join(curr_prefix))
