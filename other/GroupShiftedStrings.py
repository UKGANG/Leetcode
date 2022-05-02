'''
249. Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def hashcode(s):
            start = ord(s[0])
            return (0, *((max(ord(c) - start, ord(c) + 26 - start)) % 26 for c in s[1:])), s

        hash_list = map(hashcode, strings)
        cache = collections.defaultdict(list)
        for code, string in hash_list:
            cache[code].append(string)
        return cache.values()


assert_value([["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]],
             Solution().groupStrings,
             strings=["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
assert_value([["a"]], Solution().groupStrings, strings=["a"])
