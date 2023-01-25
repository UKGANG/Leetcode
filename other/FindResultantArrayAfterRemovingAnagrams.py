"""
2273. Find Resultant Array After Removing Anagrams
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/
"""
from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        hashed_words = [(sorted(word), word) for word in words]
        i = 1
        while i < len(hashed_words):
            if hashed_words[i - 1][0] == hashed_words[i][0]:
                del hashed_words[i]
            else:
                i += 1

        return [word for hashcode, word in hashed_words]
