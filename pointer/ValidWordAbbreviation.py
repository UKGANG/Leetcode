'''
637 · Valid Word Abbreviation
https://www.lintcode.com/problem/637/
'''
from typing import List

from test_tool import assert_value


class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """

    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        # write your code here
        l, r = 0, 0
        z = 0
        for idx in range(len(abbr)):
            if abbr[idx].isnumeric():
                r += 1
            else:
                if l == r:
                    l += 1
                    r += 1
                    z += 1
                else:
                    if abbr[l] == '0':
                        return False
                    z += int(abbr[l:r])
                    if word[z] != abbr[r]:
                        return False
                    z += 1
                    r += 1
                    l = r

        if r > l:
            if abbr[l] == '0':
                return False
            z += int(abbr[l:r])
            return z == len(word)
        return True


assert_value(True, Solution().valid_word_abbreviation, word="internationalization", abbr="i12iz4n")
assert_value(False, Solution().valid_word_abbreviation, word="apple", abbr="a2e")
assert_value(False, Solution().valid_word_abbreviation, word="a", abbr="01")
assert_value(False, Solution().valid_word_abbreviation, word="aa", abbr="a2")
assert_value(True, Solution().valid_word_abbreviation, word="a", abbr="1")
