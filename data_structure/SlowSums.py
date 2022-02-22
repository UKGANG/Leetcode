'''
Slow Sums
https://leetcode.com/discuss/general-discussion/590101/slow-sum
'''
import heapq
from typing import List

from test_tool import assert_value


def getTotalTime(arr):
    if len(arr) < 3:
        return sum(arr)
    arr = [-i for i in arr]
    heapq.heapify(arr)
    res = 0

    while len(arr) > 1:
        cnt = heapq.heappop(arr)
        cnt += heapq.heappop(arr)
        res -= cnt
        heapq.heappush(arr, cnt)
    return res


assert_value(26, getTotalTime, arr=[4, 2, 1, 3])
