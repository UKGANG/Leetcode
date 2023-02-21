"""
Complementary Pairs

"""
import collections
from typing import List


class Solution:
    def complementaryPairs(self, words: List[str]) -> List[List[int]]:
        def hashcode(word: str) -> int:
            code = 0
            for c in word:
                code ^= 1 << (ord(c) - ord('a'))
            return code

        hashed_count = collections.Counter()
        for word in words:
            hashed_count[hashcode(word)] += 1

        res_1 = 0
        for k, v in hashed_count.items():
            if v > 1:
                res_1 += v * (v - 1)
        res_2 = 0
        for k, v in hashed_count.items():
            for i in range(26):
                new_k = (1 << i) ^ k
                if new_k not in hashed_count:
                    continue
                res_2 += v * hashed_count[new_k]
        return (res_1 + res_2) >> 1
