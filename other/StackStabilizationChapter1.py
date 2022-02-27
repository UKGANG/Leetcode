'''
Stack Stabilization (Chapter 1)

'''
from typing import List

from test_tool import assert_value


def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    res = 0
    while True:
        found = False
        for i in range(N - 1):
            idx = N - i - 2
            if R[idx] >= R[idx + 1]:
                R[idx] = R[idx + 1] - 1
                if R[idx] <= 0:
                    return -1
                res += 1
                found = True
        if not found:
            break
    return res


assert_value(3, getMinimumDeflatedDiscCount, N=5, R=[2, 5, 3, 6, 5])
assert_value(2, getMinimumDeflatedDiscCount, N=3, R=[100, 100, 100])
assert_value(-1, getMinimumDeflatedDiscCount, N=4, R=[6, 5, 4, 3])
