'''
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/
'''
from typing import List, NoReturn, Optional

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_arr = self.pre_order(root)
        sub_root_arr = self.pre_order(subRoot)
        kmp_arr = self.build_kmp_idx(sub_root_arr)
        pre_order_check = self.kmp_check(root_arr, sub_root_arr, kmp_arr)

        root_arr = self.in_order(root)
        sub_root_arr = self.in_order(subRoot)
        kmp_arr = self.build_kmp_idx(sub_root_arr)
        in_order_check = self.kmp_check(root_arr, sub_root_arr, kmp_arr)

        return pre_order_check and in_order_check

    def kmp_check(self, root_arr: List[str], sub_root_arr: List[str], kmp_arr: List[str]) -> bool:
        l = 0
        for r in range(len(root_arr)):
            while l > 0 and sub_root_arr[l] != root_arr[r]:
                l = kmp_arr[l - 1]
            if sub_root_arr[l] == root_arr[r]:
                l += 1
            if l == len(kmp_arr):
                return True
        return False

    def build_kmp_idx(self, target_arr: List[str]) -> List[str]:
        kmp_arr = [0] * len(target_arr)
        l = 0
        for r in range(1, len(target_arr)):
            while l > 0 and target_arr[l] != target_arr[r]:
                l = kmp_arr[l - 1]
            if target_arr[l] == target_arr[r]:
                l += 1
            kmp_arr[r] = l
        return kmp_arr

    def pre_order(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            if not curr.left:
                res.append('L')
            else:
                stack.append(curr.left)
            if not curr.right:
                res.append('R')
            else:
                stack.append(curr.right)
        return res

    def in_order(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                if not curr.left:
                    res.append('L')
                res.append(curr.val)
                if not curr.right:
                    res.append('R')
                curr = curr.right
        return res
