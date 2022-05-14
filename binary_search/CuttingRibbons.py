'''
1891. Cutting Ribbons
https://leetcode.com/problems/cutting-ribbons/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        total = sum(ribbons)
        if total < k:
            return 0
        l, r = 1, total // k
        while l <= r:
            m = (l + r) >> 1
            cnt = 0
            for ribbon in ribbons:
                cnt += ribbon // m
            if cnt >= k:
                l = m + 1
            else:
                r = m - 1

        return r


assert_value(5, Solution().maxLength, ribbons=[9, 7, 5], k=3)
assert_value(4, Solution().maxLength, ribbons=[7, 5, 9], k=4)
assert_value(0, Solution().maxLength, ribbons=[5, 7, 9], k=22)
