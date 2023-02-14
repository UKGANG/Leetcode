'''
Rotary Lock (Chapter 2)

'''
from typing import List

from test_tool import assert_value
from functools import lru_cache


def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    queue = {(1, 1): 0}
    for code in C:
        next_queue = {}
        for (n1, n2), prev_cost in queue.items():
            n1_diff = abs(n1 - code)
            n1_cost = min(n1_diff, N - n1_diff)
            n1_next, n2_next = sorted([code, n2])
            curr_cost = n1_cost + prev_cost
            if (n1_next, n2_next) in next_queue:
                if next_queue[(n1_next, n2_next)] > curr_cost:
                    del next_queue[(n1_next, n2_next)]
            if (n1_next, n2_next) not in next_queue:
                next_queue[(n1_next, n2_next)] = curr_cost
            n2_diff = abs(n2 - code)
            n2_cost = min(n2_diff, N - n2_diff)
            n1_next, n2_next = sorted([code, n1])
            curr_cost = n2_cost + prev_cost
            if (n1_next, n2_next) in next_queue:
                if next_queue[(n1_next, n2_next)] > curr_cost:
                    del next_queue[(n1_next, n2_next)]
            if (n1_next, n2_next) not in next_queue:
                next_queue[(n1_next, n2_next)] = curr_cost
        queue = next_queue
    return min(queue.values())


def _getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    @lru_cache(None)
    def backtrack(n1, n2, i):
        if i == len(C):
            return 0
        res1 = min(abs(n1 - C[i]), N - abs(n1 - C[i])) + backtrack(C[i], n2, i + 1)
        res2 = min(abs(n2 - C[i]), N - abs(n2 - C[i])) + backtrack(n1, C[i], i + 1)
        return min(res1, res2)

    return backtrack(1, 1, 0)


def __getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
    C = [1] + C
    costs = [0]
    for i in range(1, M + 1):
        costs.append(min(costs[j] + get_cost(C[j], C[i], N) for j in range(i)))
        for j in range(i):
            costs[j] += get_cost(C[i - 1], C[i], N)
    return min(costs)


def get_cost(orig, dest, N):
    return min(abs(orig - dest), N - abs(orig - dest))


assert_value(2, getMinCodeEntryTime, N=3, M=3, C=[1, 2, 3])
assert_value(6, getMinCodeEntryTime, N=10, M=4, C=[9, 4, 4, 8])
