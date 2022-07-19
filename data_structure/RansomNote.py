'''
383. Ransom Note
https://leetcode.com/problems/ransom-note/
'''
import collections
import itertools
import re
from typing import List

from test_tool import assert_value


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_cnt = collections.Counter(ransomNote)
        magazine_cnt = collections.Counter(magazine)
        for k, v in ransomNote_cnt.items():
            if k not in magazine_cnt:
                return False
            if magazine_cnt[k] < v:
                return False
        return True


assert_value(False, Solution().canConstruct, ransomNote="a", magazine="b")
assert_value(False, Solution().canConstruct, ransomNote="aa", magazine="ab")
assert_value(True, Solution().canConstruct, ransomNote="aa", magazine="aab")
