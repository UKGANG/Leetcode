'''
501. Find Mode in Binary Search Tree
https://leetcode.com/problems/find-mode-in-binary-search-tree/
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
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            if root.left:
                for i in traverse(root.left):
                    yield i
            yield root
            if root.right:
                for i in traverse(root.right):
                    yield i

        if not root:
            return []
        res, prev, curr_cnt, max_cnt = [], None, 0, 0
        for node in traverse(root):
            if prev is None:
                prev = node.val
            if prev == node.val:
                curr_cnt += 1
            else:
                curr_cnt = 1
                prev = node.val
            if curr_cnt == max_cnt:
                res.append(node.val)
            elif curr_cnt > max_cnt:
                res.clear()
                res.append(node.val)
                max_cnt = curr_cnt

        return res

    def _findMode(self, root: Optional[TreeNode]) -> List[int]:
        def traverse(root):
            global res, prev_val, curr_cnt, curr_max
            if root.left:
                traverse(root.left)
            if prev_val is None:
                prev_val = root.val
                curr_cnt = 1
                curr_max = 1
            else:
                if prev_val == root.val:
                    curr_cnt += 1
                else:
                    prev_val = root.val
                    curr_cnt = 1

            if curr_max == curr_cnt:
                res[root.val] = curr_cnt
            elif curr_max < curr_cnt:
                res.clear()
                res[root.val] = curr_cnt
                curr_max = curr_cnt

            if root.right:
                traverse(root.right)

        if not root:
            return []
        global res, prev_val, curr_cnt, curr_max
        res, prev_val, curr_cnt, curr_max = collections.Counter(), None, 0, None
        traverse(root)
        return res.keys()

    def __findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = collections.Counter()
        stack = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                freq[curr.val] += 1
                curr = curr.right

        freq_cnt = [f for k, f in sorted(freq.items(), key=lambda item: -item[1])][0]
        return [k for k, f in freq.items() if f == freq_cnt]
