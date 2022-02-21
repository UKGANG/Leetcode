'''
Magical Candy Bags
https://leetcode.com/discuss/interview-question/1184501/facebook-recruiting-portal-magical-candy-bags
'''
import heapq
from typing import List

from test_tool import assert_value


def maxCandies(arr, k):
    h = []
    for i in arr:
        heapq.heappush(h, -i)

    res = 0
    for i in range(k):
        n = -heapq.heappop(h)
        res += n
        n = n >> 1
        heapq.heappush(h, -n)

    return res


assert_value(14, maxCandies, arr=[2, 1, 7, 4, 2], k=3)
