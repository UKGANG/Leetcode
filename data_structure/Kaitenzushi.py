'''
Kaitenzushi
https://leetcode.com/discuss/interview-question/1682612/facebook-online-puzzle-kaitenzushi-puzzle-question
'''
import collections
from typing import List

from test_tool import assert_value


def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
    q = collections.deque()
    cache = set()
    res = 0
    for d in D:
        if d not in cache:
            q.append(d)
            cache.add(d)
            res += 1
        if len(q) > K:
            cache.remove(q.popleft())
    return res


assert_value(5, getMaximumEatenDishCount, N=6, D=[1, 2, 3, 3, 2, 1], K=1)
assert_value(4, getMaximumEatenDishCount, N=6, D=[1, 2, 3, 3, 2, 1], K=2)
assert_value(2, getMaximumEatenDishCount, N=7, D=[1, 2, 1, 2, 1, 2, 1], K=2)
