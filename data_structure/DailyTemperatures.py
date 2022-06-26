'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
'''
import collections
import heapq
from operator import itemgetter
from typing import List, Optional, Tuple

from test_tool import assert_value


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = []
        for idx in range(len(res) - 1, -1, -1):
            while s and temperatures[s[-1]] <= temperatures[idx]:
                s.pop()
            if s:
                res[idx] = s[-1] - idx
            s.append(idx)
        return res


assert_value([1, 1, 4, 2, 1, 1, 0, 0], Solution().dailyTemperatures, temperatures=[73, 74, 75, 71, 69, 72, 76, 73])
assert_value([1, 1, 1, 0], Solution().dailyTemperatures, temperatures=[30, 40, 50, 60])
assert_value([1, 1, 0], Solution().dailyTemperatures, temperatures=[30, 60, 90])
assert_value([8, 1, 5, 4, 3, 2, 1, 1, 0, 0], Solution().dailyTemperatures,
             temperatures=[89, 62, 70, 58, 47, 47, 46, 76, 100, 70])
