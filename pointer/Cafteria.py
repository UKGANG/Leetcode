'''
Cafeteria
https://leetcode.com/discuss/interview-question/1376859/facebook-puzzle
'''
from typing import List

from test_tool import assert_value


def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    res = 0
    S = sorted(S)
    for i in range(1, M):
        res += (S[i] - S[i - 1] - 1 - K) // (K + 1)
    res += (S[0] - 1) // (K + 1)
    res += (N - S[-1]) // (K + 1)
    return res


assert_value(3, getMaxAdditionalDinersCount, N=10, K=1, M=2, S=[2, 6])
assert_value(1, getMaxAdditionalDinersCount, N=15, K=2, M=3, S=[11, 6, 4])
