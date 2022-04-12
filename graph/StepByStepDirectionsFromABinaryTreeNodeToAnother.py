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
        cache_start = []
        self.find(root, startValue, cache_start)
        cache_dest = []
        self.find(root, destValue, cache_dest)
        cache_start = cache_start[::-1]
        cache_dest = cache_dest[::-1]
        i = 0

        while i < len(cache_start) and i < len(cache_dest) and cache_start[i][1] == cache_dest[i][1]:
            i += 1

        dest = cache_dest[i:]
        start = 'U' * (len(cache_start) - i)
        dest = ''.join([d for d, v in dest])

        return start + dest

    def find(self, root: TreeNode, target: int, cache: List[Tuple[str, int]]) -> bool:
        if not root:
            return False
        if root.val == target:
            cache.append([None, root.val])
            return True
        left = self.find(root.left, target, cache)
        if left:
            cache[-1][0] = 'L'
            cache.append([None, root.val])
            return True
        right = self.find(root.right, target, cache)
        if right:
            cache[-1][0] = 'R'
            cache.append([None, root.val])
            return True
