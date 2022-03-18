'''
129. Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/
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
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self._sumNumbers(root, 0)

    def _sumNumbers(self, root: Optional[TreeNode], pre: int) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return pre * 10 + root.val

        left = self._sumNumbers(root.left, pre * 10 + root.val)
        right = self._sumNumbers(root.right, pre * 10 + root.val)
        return left + right


node_2 = TreeNode(2)
node_3 = TreeNode(3)
root = TreeNode(1, node_2, node_3)
assert_value(25, Solution().sumNumbers, root=root)

node_5 = TreeNode(5)
node_1 = TreeNode(1)
node_9 = TreeNode(9, node_5, node_1)
node_0 = TreeNode(0)
root = TreeNode(4, node_9, node_0)
assert_value(1026, Solution().sumNumbers, root=root)
