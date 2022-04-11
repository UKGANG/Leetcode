'''
366. Find Leaves of Binary Tree
https://leetcode.com/problems/find-leaves-of-binary-tree/
'''
import collections
from operator import itemgetter
from typing import List, Optional

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = collections.defaultdict(list)

        def dfs(node, res):
            if not node:
                return 0
            level = max(dfs(node.left, res), dfs(node.right, res)) + 1
            res[level].append(node.val)
            return level

        dfs(root, res)
        return [v for k, v in sorted(res.items(), key=itemgetter(0))]


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node2.left = node4
node2.right = node5

node1.left = node2
node1.right = node3

Solution().findLeaves(node1)
assert_value([[4, 5, 3], [2], [1]], Solution().findLeaves, root=node1)
