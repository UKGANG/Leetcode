'''
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {n: i for i, n in enumerate(inorder)}

        def backtrack(start_inorder, end_inorder, mid_preorder):
            if start_inorder == end_inorder:
                return None
            res = TreeNode(preorder[mid_preorder])
            mid_inorder = inorder_idx[preorder[mid_preorder]]
            res.left = backtrack(start_inorder, mid_inorder, mid_preorder + 1)
            res.right = backtrack(mid_inorder + 1, end_inorder, mid_preorder + mid_inorder - start_inorder + 1)
            return res

        return backtrack(0, len(preorder), 0)
