'''
299. Bulls and Cows
https://leetcode.com/problems/bulls-and-cows/
'''
from collections import Counter
from typing import List

from test_tool import assert_value


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = set()
        cow = Counter()
        for idx, (s, g) in enumerate(zip(secret, guess)):
            if s == g:
                bull.add(idx)
            else:
                cow[s] += 1

        A = len(bull)
        B = 0
        for idx, g in enumerate(guess):
            if idx in bull:
                continue
            if cow[g]:
                cow[g] -= 1
                B += 1

        return f'{A}A{B}B'


assert_value("1A3B", Solution().getHint, secret="1807", guess="7810")
assert_value("1A1B", Solution().getHint, secret="1123", guess="0111")
