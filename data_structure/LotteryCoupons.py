"""
Lottery Coupons
https://leetcode.com/discuss/interview-question/356402/Google-or-OA-2018-or-Lottery-Game
"""
import collections
from typing import List
from test_tool import assert_value


class Solution:
    def lotteryCoupon(self, coupons: List[int]) -> int:
        arr_group = collections.defaultdict(list)
        for idx, n in enumerate(coupons):
            arr_group[n].append(idx)
        res = len(coupons) + 1
        for n, indices in arr_group.items():
            if len(indices) < 2:
                continue
            for i in range(1, len(indices)):
                res = min(res, indices[i] - indices[i - 1] + 1)

        return res if res <= len(coupons) else -1


assert_value(4, Solution().lotteryCoupon, coupons=[5, 3, 4, 2, 3, 4, 5, 7])
assert_value(-1, Solution().lotteryCoupon, coupons=[3, 6, 1, 9])
