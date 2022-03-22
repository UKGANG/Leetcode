'''
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = ['']
        for n in digits:
            res_new = []
            for w in self._mapping[n]:
                for comb in res:
                    res_new.append(comb + w)
            res = res_new
        return sorted(res)


assert_value(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], Solution().letterCombinations, digits="23")
assert_value([], Solution().letterCombinations, digits="")
