'''
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
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
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = []
        curr = root
        res = 0
        while True:
            while curr:
                stack.append(curr)
                if curr.val < low:
                    break
                curr = curr.left
            if not stack:
                break
            curr = stack.pop()
            if curr.val > high:
                curr = None
                continue
            if low <= curr.val <= high:
                res += curr.val
            curr = curr.right
        return res


node0 = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node10 = TreeNode(10)
node15 = TreeNode(15)
node18 = TreeNode(18)

node5.left = node3
node5.right = node7

node15.right = node18

node10.left = node5
node10.right = node15
node3.right = node1

assert_value(32, Solution().rangeSumBST, root=node10, low=7, high=15)
