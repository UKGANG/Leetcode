'''
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
'''
import collections
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
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)
        return res

    def _rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        curr_level = collections.deque([root])
        while curr_level:
            size = len(curr_level)
            for i in range(size):
                curr = curr_level.popleft()
                if curr.left:
                    curr_level.append(curr.left)
                if curr.right:
                    curr_level.append(curr.right)
                if i == size - 1:
                    res.append(curr.val)

        return res

    def __rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = {}
        self._traverse(root, 0, res)
        return [item[1].val for item in sorted(res.items())]

    def _traverse(self, node: Optional[TreeNode], level: int, cache: dict):
        if not node:
            return
        self._traverse(node.left, level + 1, cache)
        cache[level] = node
        self._traverse(node.right, level + 1, cache)


assert_value(["a"], Solution().findWords, board=[["a"]], words=["a"])
