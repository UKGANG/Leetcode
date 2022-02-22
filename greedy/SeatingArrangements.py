'''
Seating Arrangements
https://leetcode.com/discuss/interview-question/709517/facebook-recruiting-portal-seating-arrangements
'''
import heapq
from typing import List

from test_tool import assert_value


def minOverallAwkwardness(arr):
    heapq.heapify(arr)
    cache = [heapq.heappop(arr)]

    res = 0
    while arr:
        head, tail = cache[0], cache[-1]
        curr = heapq.heappop(arr)
        if head < tail:
            res = max(res, curr - head)
            cache.insert(0, curr)
        else:
            res = max(res, curr - tail)
            cache.append(curr)
    return res


assert_value(4, minOverallAwkwardness, arr=[5, 10, 6, 8])
