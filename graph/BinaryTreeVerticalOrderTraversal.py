'''
987. Vertical Order Traversal of a Binary Tree
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
'''
import collections
import heapq
from operator import itemgetter
from typing import List, Optional

from test_tool import assert_value

"""
Definition of TreeNode:
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        cache = collections.defaultdict(list)
        q_curr = [(0, root)]
        row = 0
        while q_curr:
            q_next = []
            for level, node in q_curr:
                heapq.heappush(cache[level], (row, node.val))
                if node.left:
                    q_next.append((level - 1, node.left))
                if node.right:
                    q_next.append((level + 1, node.right))
            row += 1
            q_curr = q_next

        res = []
        for level, items in sorted(cache.items(), key=itemgetter(0)):
            curr = []
            while items:
                row, val = heapq.heappop(items)
                curr.append(val)
            res.append(curr)

        return res


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node6

node3.left = node5
node3.right = node7

assert_value([[4], [2], [1, 5, 6], [3], [7]], Solution().verticalTraversal, root=node1)
