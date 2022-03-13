'''
Hops
https://leetcode.com/discuss/interview-question/1641064/facebook-director-of-photography-puzzle-overflow
'''
from typing import List

from test_tool import assert_value


def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    P = sorted(P)
    left, right = P[0], P[0]
    res = 0
    # Form a group
    for p in P[1:]:
        res += (p - right - 1)
        left += (p - right - 1)
        right = p
    res += (N - right - 1)
    res += (right - left + 1)
    return F + (N - F - 1) - (min(P) - 1)


def getSecondsRequired_v2(N: int, F: int, P: List[int]) -> int:
    return N - min(P)


assert_value(2, getSecondsRequired, N=3, F=1, P=[1])
assert_value(4, getSecondsRequired, N=6, F=3, P=[5, 2, 4])
