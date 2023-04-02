"""
1653. Minimum Deletions to Make String Balanced
https://leetcode.com/problems/minimum-deletions-to-make-string-balanced
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        res = b_count = 0
        for c in s:
            if c == 'b':
                b_count += 1
            else:
                res = min(res + 1, b_count)

        return res
