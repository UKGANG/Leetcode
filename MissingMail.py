'''
Missing Mail

'''
import sys
from typing import List

from test_tool import assert_value
from functools import lru_cache


def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    if S == 0:
        return max(0, sum(V) - C)
    if S == 1:
        return sum(v - C for v in V if v - C > 0)

    @lru_cache(None)
    def get_suboptimal(day, mailbox_value):
        if day == N:
            return 0
        score = 0
        if mailbox_value + V[day] > C:
            score = mailbox_value + V[day] - C + get_suboptimal(day + 1, 0)
        return max(
            score,
            get_suboptimal(day + 1, (mailbox_value + V[day]) * (1 - S))
        )

    sys.setrecursionlimit(8100)
    return get_suboptimal(0, 0)


def _getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
    if S == 0:
        return max(0, sum(V) - C)
    if S == 1:
        return sum(v - C for v in V if v - C > 0)
    V.insert(0, 0)
    residual_ratio = []
    for i in range(N + 1):
        residual_ratio.append((1 - S) ** i)
    pre_sum = [0]
    for i in range(1, N + 1):
        pre_sum.append(V[i] * residual_ratio[-i])
    for i in range(N):
        pre_sum[i + 1] += pre_sum[i]
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] - C + (pre_sum[i] - pre_sum[j]) / residual_ratio[-i])
    return max(dp)


assert_value(25., getMaxExpectedProfit, N=5, V=[10, 2, 8, 6, 4], C=5, S=0.0)
assert_value(9., getMaxExpectedProfit, N=5, V=[10, 2, 8, 6, 4], C=5, S=1.0)
assert_value(17., getMaxExpectedProfit, N=5, V=[10, 2, 8, 6, 4], C=3, S=0.5)
assert_value(20.10825000, getMaxExpectedProfit, N=5, V=[10, 2, 8, 6, 4], C=3, S=0.15)
