"""
290. Word Pattern
https://leetcode.com/problems/word-pattern
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        idx_pattern = {}
        word_pattern = {}
        word_list = s.split(' ')
        if len(word_list) != len(pattern):
            return False
        for idx, (c, word) in enumerate(zip(pattern, word_list)):
            print(c, word)
            if c not in idx_pattern:
                idx_pattern[c] = idx
            if word not in word_pattern:
                word_pattern[word] = idx
            if idx_pattern[c] == word_pattern[word]:
                continue
            return False
        else:
            return True
