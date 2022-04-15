'''
843. Guess the Word
https://leetcode.com/problems/guess-the-word/
'''
from typing import List

from random import random
from test_tool import assert_value


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        while True:
            candidate = wordlist[int(random() * len(wordlist))]
            n = master.guess(candidate)
            if 6 == n:
                break
            if 0 == n:
                i = 0
                while i < len(wordlist):
                    matched = sum(a == b for a, b in zip(wordlist[i], candidate))
                    if matched:
                        del wordlist[i]
                    else:
                        i += 1
            else:
                i = 0
                while i < len(wordlist):
                    match_cnt = sum(a == b for a, b in zip(wordlist[i], candidate))
                    if match_cnt != n:
                        del wordlist[i]
                    else:
                        i += 1
