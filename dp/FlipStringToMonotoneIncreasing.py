"""
926. Flip String to Monotone Increasing
https://leetcode.com/problems/flip-string-to-monotone-increasing
"""


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = one_count = 0
        for c in s:
            if c == '1':
                one_count += 1
            else:
                res = min(res + 1, one_count)
        return res
