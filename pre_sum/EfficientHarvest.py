'''
Efficient Harvest
https://leetcode.com/discuss/interview-question/1321204/efficient-harvest-faang-oa-question-2021
'''
import collections
import heapq
from operator import itemgetter
from typing import List, Optional, Tuple

from test_tool import assert_value


class Solution:
    def efficientHarvest(self, arr: List[int], k: int) -> int:
        n = len(arr) >> 1
        pair = [arr[i] + arr[i + n] for i in range(n)]
        pre_sum = [0]
        sum_curr = 0
        for acre in pair + pair[:k - 1]:
            sum_curr += acre
            pre_sum.append(sum_curr)

        res = None
        for i in range(k, len(pre_sum)):
            diff = pre_sum[i] - pre_sum[i - k]
            if res is None:
                res = diff
            else:
                res = max(res, diff)

        return res


assert_value(16, Solution().efficientHarvest, arr=[1, 5, 1, 3, 7, - 3], k=2)
assert_value(0, Solution().efficientHarvest, arr=[-3, 6, 3, -6], k=1)
assert_value(-2, Solution().efficientHarvest, arr=[-5, 3], k=1)
