"""
1408. String Matching in an Array
https://leetcode.com/problems/string-matching-in-an-array/
"""
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort()
        res = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if words[i] in words[j]:
                    res.append(words[i])
                    break
        return res
