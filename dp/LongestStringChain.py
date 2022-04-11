'''
1048. Longest String Chain
https://leetcode.com/problems/longest-string-chain/
'''
from typing import List, Optional

from test_tool import assert_value


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=len)
        cache = {}
        for word in words:
            for i in range(len(word)):
                key = word[:i] + word[i + 1:]
                cache[word] = cache.get(word, 0)
                cnt = cache.get(key, 0) + 1
                cache[word] = max(cnt, cache[word])

        return max(cache.values())


assert_value(4, Solution().longestStrChain, words=["a", "b", "ba", "bca", "bda", "bdca"])
assert_value(5, Solution().longestStrChain, words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"])
assert_value(1, Solution().longestStrChain, words=["abcd", "dbqca"])
#
