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
        def backtrack(idx):
            if len(curr) == len(digits):
                if curr:
                    res.append(''.join(curr))
                return
            for c in self._mapping[digits[idx]]:
                curr.append(c)
                backtrack(idx + 1)
                curr.pop()

        res, curr = [], []
        backtrack(0)
        return res

    def letterCombinations_v3(self, digits: str) -> List[str]:
        if not digits:
            return []
        return self.generate(digits, 0)

    def generate(self, digits, i):
        if i == len(digits) - 1:
            return self._mapping[digits[-1]].copy()
        res = []
        for combo in self.generate(digits, i + 1):
            for c in self._mapping[digits[i]]:
                res.append(f'{c}{combo}')
        return res

    def letterCombinations_v2(self, digits: str) -> List[str]:
        def backtrack(idx):
            if curr and len(curr) == len(digits):
                res.append(''.join(curr))
                return
            for i in range(idx, len(digits)):
                for c in self._mapping[digits[i]]:
                    curr.append(c)
                    backtrack(i + 1)
                    curr.pop()

        res, curr = [], []
        backtrack(0)
        return res

    def letterCombinations_v1(self, digits: str) -> List[str]:
        def backtrack(l, r, n):
            nonlocal res, combo
            if not n and combo:
                res.append(combo[:])
                return
            for i in range(l, r + 1):
                num = digits[i]
                for j in self._mapping[num]:
                    combo.append(j)
                    backtrack(i + 1, r, n - 1)
                    combo.pop()

        res = []
        combo = []
        backtrack(0, len(digits) - 1, len(digits))
        return [''.join(combo) for combo in res]

    def letterCombinations_v0(self, digits: str) -> List[str]:
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
