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

    def _canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote: str = sorted(ransomNote)
        magazine: str = sorted(magazine)
        l, r = 0, 0
        while l < len(ransomNote) and r < len(magazine):
            if magazine[r] != ransomNote[l]:
                if ord(magazine[r]) > ord(ransomNote[l]):
                    return False
                r += 1
                continue
            else:
                l += 1
                r += 1
        return l == len(ransomNote)


assert_value(False, Solution().canConstruct, ransomNote="a", magazine="b")
assert_value(False, Solution().canConstruct, ransomNote="aa", magazine="ab")
assert_value(True, Solution().canConstruct, ransomNote="aa", magazine="aab")
assert_value(True, Solution().canConstruct, ransomNote="bg",
             magazine="efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")
