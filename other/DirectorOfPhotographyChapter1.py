'''
Director of Photography (Chapter 1)
https://leetcode.com/discuss/interview-question/1641064/facebook-director-of-photography-puzzle-overflow
'''
from typing import List

from test_tool import assert_value


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    left = countLeft(N, C, X, Y)
    right = countLeft(N, C[::-1], X, Y)

    return left + right


def countLeft(N: int, C: str, X: int, Y: int) -> int:
    res = 0
    for idx, p in enumerate(C):
        if p == 'P':
            for d in range(X, Y + 1):
                if idx + d >= N:
                    break
                if C[idx + d] != 'A':
                    continue
                for b in range(X, Y + 1):
                    if idx + d + b >= N:
                        break
                    if C[idx + d + b] == 'B':
                        res += 1

    return res


assert_value(1, getArtisticPhotographCount, N=5, C='APABA', X=1, Y=2)
assert_value(0, getArtisticPhotographCount, N=5, C='APABA', X=2, Y=3)
assert_value(3, getArtisticPhotographCount, N=8, C='.PBAAP.B', X=1, Y=3)
