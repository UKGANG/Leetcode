'''
Rotary Lock (Chapter 2)

'''
from typing import List

from test_tool import assert_value


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    C = [1] + C
    costs = [0]
    for i in range(1, M+1):
        costs.append(min(costs[j] + get_cost(C[j], C[i], N) for j in range(i)))
        for j in range(i):
            costs[j] += get_cost(C[i - 1], C[i], N)
    return min(costs)


def get_cost(orig, dest, N):
    return min(abs(orig - dest), N - abs(orig - dest))


# assert_value(2, getMinCodeEntryTime, N=3, M=3, C=[1, 2, 3])
assert_value(6, getMinCodeEntryTime, N=10, M=4, C=[9, 4, 4, 8])
