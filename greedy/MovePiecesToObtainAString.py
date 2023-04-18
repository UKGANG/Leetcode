"""
2337. Move Pieces to Obtain a String
https://leetcode.com/problems/move-pieces-to-obtain-a-string
"""


class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace('_', '') != target.replace('_', ''):
            return False
        idx_start = 0
        idx_target = 0
        while idx_start < len(start) and idx_target < len(target):
            while idx_start < len(start) and start[idx_start] == '_':
                idx_start += 1
            while idx_target < len(target) and target[idx_target] == '_':
                idx_target += 1

            if idx_start == len(start) and idx_target == len(target):
                break
            if start[idx_start] == 'L' and idx_start < idx_target:
                return False
            if start[idx_start] == 'R' and idx_start > idx_target:
                return False
            idx_start += 1
            idx_target += 1
        return True
