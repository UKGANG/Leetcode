"""
1347. Minimum Number of Steps to Make Two Strings Anagram
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/description/
"""
import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt_s = collections.Counter(s)
        cnt_t = collections.Counter(t)
        for k, v in cnt_t.items():
            if k not in cnt_s:
                continue
            cnt_s[k] -= cnt_t[k]
        return sum(v for v in cnt_s.values() if v > 0)
