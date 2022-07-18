'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = collections.Counter(s)
        t_cnt = collections.Counter(t)

        if len(s_cnt) != len(t_cnt):
            return False

        for k, v in s_cnt.items():
            if v != t_cnt[k]:
                return False
        return True

    def _isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


assert_value(True, Solution().isAnagram, s="anagram", t="nagaram")
assert_value(False, Solution().isAnagram, s="rat", t="car")
