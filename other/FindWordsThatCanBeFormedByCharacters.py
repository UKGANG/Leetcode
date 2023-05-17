"""
1160. Find Words That Can Be Formed by Characters
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters
"""
import collections
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_cnt = collections.Counter(chars)
        res = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c, cnt in word_cnt.items():
                if char_cnt[c] < cnt:
                    break
            else:
                res += len(word)

        return res
