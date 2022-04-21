'''
173. Binary Search Tree Iterator
https://leetcode.com/problems/binary-search-tree-iterator/
'''
from typing import List, Optional, Tuple

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self._root = root
        self._curr = root
        self._stack = [root]

    def next(self) -> int:
        while self._curr:
            if self._curr.left:
                self._stack.append(self._curr.left)
            self._curr = self._curr.left
        if not self._stack:
            return None
        res = self._stack.pop()
        self._curr = res
        if self._curr.right:
            self._stack.append(self._curr.right)
        self._curr = self._curr.right
        return res.val

    def hasNext(self) -> bool:
        return self._stack or self._curr


class BSTIteratorV2:

    def __init__(self, root: Optional[TreeNode]):
        self._iter = self.dfs(root)
        self._buffer = None

    def dfs(self, root):
        if not root:
            return
        if root.left:
            for res in self.dfs(root.left):
                yield res
        yield root
        if root.right:
            for res in self.dfs(root.right):
                yield res

    def next(self) -> int:
        res = None
        if self.hasNext():
            res = self._buffer
            self._buffer  = None
        return res.val if res else -1

    def hasNext(self) -> bool:
        if self._buffer:
            return True
        try:
            self._buffer = next(self._iter)
        except StopIteration as e:
            return False
        return True