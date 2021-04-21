'''
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/
'''
import math
from typing import List

from test_tool import assert_value


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l = 1
        r = max(piles)
        while l <= r:
            check_point = (l + r) >> 1
            rnd = sum(math.ceil(pile / check_point) for pile in piles)
            if rnd <= H:
                r = check_point - 1
            else:
                l = check_point + 1
        return l


assert_value(4, Solution().minEatingSpeed, piles=[3, 6, 7, 11], H=8)
assert_value(30, Solution().minEatingSpeed, piles=[30, 11, 23, 4, 20], H=5)
assert_value(23, Solution().minEatingSpeed, piles=[30, 11, 23, 4, 20], H=6)
assert_value(2, Solution().minEatingSpeed, piles=[312884470], H=312884469)
