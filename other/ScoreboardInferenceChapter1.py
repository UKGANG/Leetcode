'''
Scoreboard Inference (Chapter 1)
https://leetcode.com/discuss/interview-question/1518388/facebook-career-recruiting-portal-scoreboard-inference
'''
from typing import List

from test_tool import assert_value


def getMinProblemCount(N: int, S: List[int]) -> int:
    res = sorted(S)[-1] >> 1
    return res + int(any([s & 1 for s in S]))


assert_value(4, getMinProblemCount, N=6, S=[1, 2, 3, 4, 5, 6])
assert_value(3, getMinProblemCount, N=4, S=[4, 3, 3, 4])
assert_value(4, getMinProblemCount, N=4, S=[2, 4, 6, 8])
