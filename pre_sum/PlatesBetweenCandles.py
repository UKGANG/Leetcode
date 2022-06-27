'''
2055. Plates Between Candles
https://leetcode.com/problems/plates-between-candles/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        left = [None] * len(s)
        right = [None] * len(s)
        idx = None
        for i in range(len(s)):
            if s[i] == '|':
                idx = i
            left[i] = idx
        idx = None
        for i in range(len(s)):
            i = len(s) - 1 - i
            if s[i] == '|':
                idx = i
            right[i] = idx

        pre_sum = []
        cnt = 0
        for c in s:
            if c == '*':
                cnt += 1
            pre_sum.append(cnt)

        res = [0] * len(queries)
        for idx, (start, end) in enumerate(queries):
            idx_left, idx_right = right[start], left[end]
            if idx_left is None or idx_right is None:
                continue
            if idx_left < idx_right:
                res[idx] = pre_sum[idx_right] - pre_sum[idx_left]
        return res


assert_value([2, 3], Solution().platesBetweenCandles,
             s="**|**|***|", queries=[[2, 5], [5, 9]])
assert_value([9, 0, 0, 0, 0], Solution().platesBetweenCandles,
             s="***|**|*****|**||**|*", queries=[[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]])
