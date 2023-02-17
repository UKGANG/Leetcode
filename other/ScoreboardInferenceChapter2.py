'''
Scoreboard Inference (Chapter 2)
https://leetcode.com/discuss/interview-question/1594234/facebook-career-recruiting-portal-scoreboard-inference-chapter-2
'''
from typing import List

from test_tool import assert_value

from typing import List


# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
    S.sort()
    res = S[-1] // 3
    if S[-1] % 3 == 0:
        return res + int(any([s % 3 for s in S]))
    if S[-1] % 3 == 1 and S[0] > 1 and S[-2] + 1 != S[-1]:
        return res + 1
    return res + int(any([s % 3 == 1 for s in S])) + int(any([s % 3 == 2 for s in S]))


assert_value(4, getMinProblemCount, N=6, S=[1, 2, 3, 4, 5, 6])
assert_value(3, getMinProblemCount, N=4, S=[4, 3, 3, 4])
assert_value(4, getMinProblemCount, N=4, S=[2, 4, 6, 8])
