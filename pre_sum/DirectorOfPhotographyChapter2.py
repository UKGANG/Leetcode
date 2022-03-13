'''
Director of Photography (Chapter 2)
https://leetcode.com/discuss/interview-question/1641064/facebook-director-of-photography-puzzle-overflow
'''
from typing import List

from test_tool import assert_value


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
    pre_sum_p = [0]
    pre_sum_b = [0]
    for c in C:
        if c == 'P':
            pre_sum_p.append(pre_sum_p[-1] + 1)
        else:
            pre_sum_p.append(pre_sum_p[-1])
    for c in C:
        if c == 'B':
            pre_sum_b.append(pre_sum_b[-1] + 1)
        else:
            pre_sum_b.append(pre_sum_b[-1])

    res = 0
    for idx, c in enumerate(C):
        if c != 'A':
            continue

        left_bound = bound(idx - Y, N), bound(idx - X + 1, N)
        right_bound = bound(idx + X, N), bound(idx + Y + 1, N)

        res += (pre_sum_p[left_bound[1]] - pre_sum_p[left_bound[0]]) * (
                pre_sum_b[right_bound[1]] - pre_sum_b[right_bound[0]])
        res += (pre_sum_b[left_bound[1]] - pre_sum_b[left_bound[0]]) * (
                pre_sum_p[right_bound[1]] - pre_sum_p[right_bound[0]])

    return res


def bound(idx, N):
    return max(0, min(idx, N))


assert_value(1, getArtisticPhotographCount, N=5, C='APABA', X=1, Y=2)
assert_value(0, getArtisticPhotographCount, N=5, C='APABA', X=2, Y=3)
assert_value(3, getArtisticPhotographCount, N=8, C='.PBAAP.B', X=1, Y=3)
