'''
1644. Lowest Common Ancestor of a Binary Tree II
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
'''
from typing import List

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        self.dfs(root, p, q)
        return self.res

    def dfs(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> int:
        if not node:
            return 0
        curr = node.val == p.val or node.val == q.val
        left = self.dfs(node.left, p, q)
        right = self.dfs(node.right, p, q)
        cnt = curr + left + right
        if cnt == 2 and not self.res:
            self.res = node
        return curr + left + right


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node2.left = node7
node2.right = node4

node5.left = node6
node5.right = node2

node1.left = node0
node1.right = node8

node3.left = node5
node3.right = node1

assert_value(node3, Solution().lowestCommonAncestor, root=node3, p=node5, q=node1)
assert_value(node5, Solution().lowestCommonAncestor, root=node3, p=node5, q=node4)

node1.left = node2
node1.right = node3
node2.left = None
node2.right = None
node3.left = None
node3.right = None
assert_value(node1, Solution().lowestCommonAncestor, root=node1, p=node2, q=node3)
