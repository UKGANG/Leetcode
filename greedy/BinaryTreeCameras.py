'''
968. Binary Tree Cameras
https://leetcode.com/problems/binary-tree-cameras/
'''
from typing import List, Final, Optional

from test_tool import assert_value


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def backtrack(node):
            if not node.left and not node.right:
                return 0, NOT_COVERED
            cnt_left, status_left = 0, COVERED
            cnt_right, status_right = 0, COVERED

            if node.left:
                cnt_left, status_left = backtrack(node.left)
            if node.right:
                cnt_right, status_right = backtrack(node.right)
            if NOT_COVERED in [status_left, status_right]:
                return cnt_left + cnt_right + 1, INSTALLED_CAMERA
            if INSTALLED_CAMERA in [status_left, status_right]:
                return cnt_left + cnt_right, COVERED
            return cnt_left + cnt_right, NOT_COVERED

        NOT_COVERED: Final[int] = 0
        INSTALLED_CAMERA: Final[int] = 1
        COVERED: Final[int] = 2

        cnt, status = backtrack(root)
        if status == NOT_COVERED:
            cnt += 1

        return cnt
