'''
2096. Step-By-Step Directions From a Binary Tree Node to Another
https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
'''
from typing import List, Optional, Tuple

from test_tool import assert_value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(node, val):
            if not node:
                return False
            if node.val == val:
                res.extend(curr[:])
                return True

            curr.append(('L', node.val))
            if find(node.left, val):
                return True
            curr.pop()

            curr.append(('R', node.val))
            if find(node.right, val):
                return True
            curr.pop()
            return False

        res = start = []
        curr = []
        find(root, startValue)

        res = end = []
        curr.clear()
        find(root, destValue)

        idx = 0
        while idx < min(len(start), len(end)) and start[idx][0] == end[idx][0]:
            idx += 1
        start = ['U'] * (len(start) - idx)
        end = end[idx:]
        end = [source for source, v in end]
        start.extend(end)

        return ''.join(start)

    def _getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        cache_start = []
        self.find(root, startValue, cache_start)
        cache_dest = []
        self.find(root, destValue, cache_dest)
        i = 0
        cache_start = cache_start[::-1]
        cache_dest = cache_dest[::-1]
        while i < len(cache_start) and i < len(cache_dest) and cache_start[i][0] == cache_dest[i][0]:
            i += 1

        end = [s for v, s in cache_dest[i:]]
        start = 'U' * (len(cache_start) - i)

        return start + ''.join(end)

    def find(self, root: TreeNode, target: int, cache: List[Tuple[int, str]]) -> bool:
        if not root:
            return False
        if root.val == target:
            cache.append([root.val, None])
            return True
        left = self.find(root.left, target, cache)
        if left:
            cache[-1][1] = 'L'
            cache.append([root.val, None])
            return True
        right = self.find(root.right, target, cache)
        if right:
            cache[-1][1] = 'R'
            cache.append([root.val, None])
            return True
        return False
