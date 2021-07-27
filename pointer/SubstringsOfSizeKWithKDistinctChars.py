'''
Amazon | OA 2019 | Substrings of size K with K distinct chars
https://leetcode.com/discuss/interview-question/370112
'''
from typing import List

from test_tool import assert_value


class Solution:
    def kDistinctChars(self, s: str, k) -> set:
        cache = set()
        l, r, res = 0, 0, set()
        while r < len(s):
            while len(cache) < k:
                if s[r] not in cache:
                    cache.add(s[r])
                    r += 1
                else:
                    cache.remove(s[l])
                    l += 1
            res.add(s[l:r])
            cache.remove(s[l])
            l += 1

        return res


assert_value(set(["abc", "bca", "cab"]), Solution().kDistinctChars, s="abcabc", k=3)
assert_value(set(["bac", "cab"]), Solution().kDistinctChars, s="abacab", k=3)
assert_value(set(["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]),
             Solution().kDistinctChars, s="awaglknagawunagwkwagl", k=4)
