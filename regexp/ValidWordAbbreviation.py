'''
408. Valid Word Abbreviation
https://leetcode.com/problems/valid-word-abbreviation/
'''
import re
from typing import List

from test_tool import assert_value


class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx_w = 0
        idx_l = 0
        word += 'b'
        abbr += 'b'
        for idx_r in range(len(abbr)):
            c_a = abbr[idx_r]
            if c_a.isnumeric():
                if idx_l != idx_r and abbr[idx_l] == '0':
                    return False
                continue
            if idx_l == idx_r:
                num_len = 0
            elif abbr[idx_l] == '0':
                return False
            else:
                num_len = int(abbr[idx_l:idx_r])
            idx_w += num_len
            if idx_w >= len(word):
                return False
            idx_l = idx_r + 1
            c_w = word[idx_w]
            if c_w != c_a:
                return False
            idx_w += 1
        return len(word) == idx_w

    def _validWordAbbreviation(self, word: str, abbr: str) -> bool:
        regex = ''
        l_abbr, r_abbr = 0, 1
        while r_abbr < len(abbr):
            if abbr[r_abbr].isalpha() ^ abbr[r_abbr - 1].isalpha():
                if '0' == abbr[l_abbr]:
                    return False
                regex += self.get_regexp_chunk(abbr, l_abbr, r_abbr)
                l_abbr = r_abbr
                r_abbr += 1
            else:
                r_abbr += 1

        if '0' == abbr[l_abbr]:
            return False
        regex += self.get_regexp_chunk(abbr, l_abbr, r_abbr)
        return bool(re.compile(f'^{regex}$').match(word))

    def get_regexp_chunk(self, abbr, l, r):
        sub = abbr[l: r]
        if abbr[l].isnumeric():
            n = abbr[l: r]
            return '(\w){' + n + '}'
        else:
            return sub


assert_value(True, Solution().validWordAbbreviation, word="internationalization", abbr="i12iz4n")
assert_value(False, Solution().validWordAbbreviation, word="apple", abbr="a2e")
assert_value(False, Solution().validWordAbbreviation, word="a", abbr="01")
assert_value(False, Solution().validWordAbbreviation, word="a", abbr="2")
assert_value(False, Solution().validWordAbbreviation, word="hi", abbr="1")
assert_value(True, Solution().validWordAbbreviation, word="internationalization", abbr="i5a11o1")
assert_value(False, Solution().validWordAbbreviation, word="word", abbr="w0ord")
