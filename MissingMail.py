'''
Missing Mail

'''
import sys
from typing import List

from test_tool import assert_value
from functools import lru_cache


def getMaxExpectedProfit(N: int, V: List[int], C: int, S: float) -> float:
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

    sys.setrecursionlimit(18100)
    return get_suboptimal(0, 0)


# assert_value(25., getMaxExpectedProfit, N=5, V=[10, 2, 8, 6, 4], C=5, S=0.0)
# assert_value(9., getMaxExpectedProfit, N=5, V=[10, 2, 8, 6, 4], C=5, S=1.0)
# assert_value(17., getMaxExpectedProfit, N=5, V=[10, 2, 8, 6, 4], C=3, S=0.5)
assert_value(20.10825000, getMaxExpectedProfit, N=5, V=[10, 2, 8, 6, 4], C=3, S=0.15)
