'''
792. Number of Matching Subsequences
https://leetcode.com/problems/number-of-matching-subsequences/
'''
import bisect
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        cache = collections.defaultdict(list)
        for idx, c in enumerate(s):
            cache[c].append(idx)

        res = 0
        for word in words:
            idx_s = 0
            res += 1
            for c in word:
                if c not in cache:
                    res -= 1
                    break
                idx_cache = bisect.bisect_left(cache[c], idx_s)
                if idx_cache == len(cache[c]):
                    res -= 1
                    break
                idx_s = cache[c][idx_cache] + 1

        return res

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        dp = collections.defaultdict(list)
        for idx, c in enumerate(s):
            dp[c].append(idx)

        res = 0
        for word in words:
            idx = 0
            match = True
            for c in word:
                if c not in dp:
                    match = False
                    break
                idx = bisect.bisect_left(dp[c], idx)
                if idx == len(dp[c]):
                    match = False
                    break
                idx = dp[c][idx] + 1
            if match:
                res += 1

        return res


assert_value(3, Solution().numMatchingSubseq, s="abcde", words=["a", "bb", "acd", "ace"])
assert_value(2, Solution().numMatchingSubseq, s="dsahjpjauf", words=["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"])
