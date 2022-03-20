'''
651 · Binary Tree Vertical Order Traversal
https://www.lintcode.com/problem/651/
'''
import collections
from operator import itemgetter
from typing import List

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

    def vertical_order(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = collections.defaultdict(list)
        q_curr = [(0, root)]
        while q_curr:
            q_next = []
            for level, node in q_curr:
                res[level].append(node.val)
                if node.left:
                    q_next.append((level - 1, node.left))
                if node.right:
                    q_next.append((level + 1, node.right))
            q_curr = q_next

        return [val for level, val in sorted(res.items(), key=itemgetter(0))]


