'''
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
'''
from typing import List, Optional

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = {}
        self.traverse(root, 0, res)
        return [item[1].val for item in sorted(res.items())]

    def traverse(self, node: Optional[TreeNode], level: int, cache: dict):
        if not node:
            return
        self.traverse(node.left, level + 1, cache)
        cache[level] = node
        self.traverse(node.right, level + 1, cache)


assert_value(["a"], Solution().findWords, board=[["a"]], words=["a"])
