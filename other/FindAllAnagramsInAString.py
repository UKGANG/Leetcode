"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string
"""
import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start, pending = 0, len(p)
        cache_anagram = collections.Counter(p)
        cache_curr = collections.Counter()
        res = []
        for end, c in enumerate(s):
            if c not in p:
                cache_curr.clear()
                start = end + 1
                pending = len(p)
                continue
            cache_curr[c] += 1
            pending -= 1

            while cache_curr[c] > cache_anagram[c]:
                cache_curr[s[start]] -= 1
                start += 1
                pending += 1

            if not pending:
                res.append(start)

        return res
