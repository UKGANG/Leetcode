"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/description/
"""
import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_table = collections.Counter()
        res = 0
        start = 0
        for end in range(len(s)):
            freq_table[s[end]] += 1
            if k < end - start + 1 - max(freq_table.values()):
                freq_table[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        return res
