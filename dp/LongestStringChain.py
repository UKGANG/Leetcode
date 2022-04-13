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
        res = 0
        for word in words:
            cache[word] = 0
            for i in range(len(word)):
                key = word[:i] + word[i+1:]
                if key not in cache:
                    continue
                cache[word] = max(cache[word], cache[key])
            cache[word] += 1
            res = max(res, cache[word])
        return res


assert_value(4, Solution().longestStrChain, words=["a", "b", "ba", "bca", "bda", "bdca"])
assert_value(5, Solution().longestStrChain, words=["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"])
assert_value(1, Solution().longestStrChain, words=["abcd", "dbqca"])
#
