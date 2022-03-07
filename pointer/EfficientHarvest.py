'''
Efficient Harvest | FAANG OA Question 2021
https://leetcode.com/discuss/interview-question/1321204/efficient-harvest-faang-oa-question-2021
'''
from typing import List

from test_tool import assert_value


class Solution:
    def effHarvest(self, arr: List[int], k: int) -> int:
        arr_pair = []
        n = len(arr) >> 1
        for i in range(n):
            arr_pair.append(arr[i] + arr[i + n])

        if k >= len(arr_pair):
            return sum(arr_pair)
        curr = sum(arr_pair[:k])
        res = curr
        for i in range(k, len(arr_pair)):
            curr = curr - arr_pair[i - k] + arr_pair[i]
            res = max(res, curr)

        return res


assert_value(-2, Solution().effHarvest, arr=[3, -5], k=1)
assert_value(16, Solution().effHarvest, arr=[1, 5, 1, 3, 7, -3], k=2)
assert_value(0, Solution().effHarvest, arr=[-6, 3, 6, -3], k=1)
