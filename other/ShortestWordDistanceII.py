'''
244. Shortest Word Distance II
https://leetcode.com/problems/shortest-word-distance-ii/
'''
import math
from typing import List

from test_tool import assert_value


class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.cache = {}
        for idx, word in enumerate(wordsDict):
            self.cache[word] = self.cache.get(word, [])
            self.cache[word].append(idx)

    def shortest(self, word1: str, word2: str) -> int:
        idx_word1 = self.cache[word1]
        idx_word2 = self.cache[word2]
        res = math.inf
        i, j = 0, 0
        while i < len(idx_word1) and j < len(idx_word2):
            res = min(res, abs(idx_word1[i] - idx_word2[j]))
            if idx_word1[i] > idx_word2[j]:
                j += 1
            else:
                i += 1

        return res

    def _shortest(self, word1: str, word2: str) -> int:
        idx_word1 = self.cache[word1]
        idx_word2 = self.cache[word2]
        res = float('inf')
        for x in range(len(idx_word1)):
            res_1 = float('inf')
            for y in range(len(idx_word2)):
                res_next = abs(idx_word2[y] - idx_word1[x])
                if res_1 > res_next:
                    res_1 = res_next
                else:
                    break
            res = min(res, res_1)
        return res

    def __shortest(self, word1: str, word2: str) -> int:
        idx_word1 = self.cache[word1]
        idx_word2 = self.cache[word2]
        res = float('inf')
        for x in range(len(idx_word1)):
            for y in range(len(idx_word2)):
                res = min(res, abs(idx_word2[y] - idx_word1[x]))
        return res


# Your WordDistance object will be instantiated and called as such:
obj = WordDistance(["a", "c", "b", "b", "a"])
param_1 = obj.shortest('a', 'b')
param_2 = obj.shortest('b', 'a')

assert param_1 == 1
assert param_2 == 1
