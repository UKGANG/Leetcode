'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest_str = min(strs, key=len)
        size = len(shortest_str)
        res = []
        for i in range(size):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != c:
                    return strs[0][:i]
        return shortest_str

    def longestCommonPrefix_v0(self, strs: List[str]) -> str:
        idx = 0
        len_min = len(min(strs, key=len))
        cache = set()
        while idx < len_min:
            cache.clear()
            for s in strs:
                cache.add(s[idx])
            if len(cache) > 1:
                break
            idx += 1

        return strs[0][:idx]


assert_value('fl', Solution().longestCommonPrefix, strs=["flower", "flow", "flight"])
assert_value('', Solution().longestCommonPrefix, strs=["dog", "racecar", "car"])
