'''
Rotary Lock (Chapter 1)
https://leetcode.com/discuss/interview-question/1368609/facebook-rotary-lock-practice-puzzle
'''
from typing import List

from test_tool import assert_value


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    curr = 1
    res = 0
    for c in C:
        res += min(abs(curr - c), N - abs(curr - c))
        curr = c
    return res


assert_value(2, getMinCodeEntryTime, N=3, M=3, C=[1, 2, 3])
assert_value(11, getMinCodeEntryTime, N=10, M=4, C=[9, 4, 4, 8])
