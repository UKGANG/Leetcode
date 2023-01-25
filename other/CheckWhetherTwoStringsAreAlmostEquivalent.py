"""
2068. Check Whether Two Strings are Almost Equivalent
https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
"""
from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        cnt_1 = Counter(word1)
        cnt_2 = Counter(word2)

        return max(abs(cnt_1[chr(c)] - cnt_2[chr(c)]) for c in range(ord('a'), ord('z') + 1)) < 4
