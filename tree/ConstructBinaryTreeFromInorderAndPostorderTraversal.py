'''
106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
'''
import collections
from typing import List, Optional, NoReturn

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {n: i for i, n in enumerate(inorder)}

        def backtrack(start, end, mid_postorder):
            if start == end:
                return None
            res = TreeNode(postorder[mid_postorder])
            mid_inorder = inorder_idx[postorder[mid_postorder]]
            res.left = backtrack(start, mid_inorder, mid_postorder - end + mid_inorder)
            res.right = backtrack(mid_inorder + 1, end, mid_postorder - 1)
            return res

        return backtrack(0, len(inorder), len(inorder) - 1)

