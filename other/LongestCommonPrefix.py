'''
14. Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
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
