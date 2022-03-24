'''
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if n == 0:
                return True
            if flowerbed[0] == 1:
                return False
            return n < 2
        if sum(flowerbed) == 0:
            return n <= ((len(flowerbed) + 1) >> 1)

        l, r = 0, len(flowerbed) - 1
        leading_zeros = 0
        trailing_zeros = 0
        res = 0
        while l < r and flowerbed[l] == 0:
            leading_zeros += 1
            l += 1
        res += (l >> 1)
        while l < r and flowerbed[r] == 0:
            trailing_zeros += 1
            r -= 1
        res += ((len(flowerbed) - 1 - r) >> 1)
        while l < r:
            zero_cnt = 0
            while flowerbed[l] == 0:
                l += 1
                zero_cnt += 1
            res += ((zero_cnt - 1) >> 1) if zero_cnt else 0
            l += 1

        return n <= res

    def canPlaceFlowers_v1(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        idx = 0
        while idx < len(flowerbed):
            if flowerbed[idx] == 0:
                if idx == len(flowerbed) - 1:
                    return n == 1
                if flowerbed[idx + 1] == 0:
                    n -= 1
                    idx += 2
                else:
                    idx += 3
            else:
                idx += 2
            if n == 0:
                return True

        return n == 0


assert_value(True, Solution().canPlaceFlowers, flowerbed=[0, 0, 0], n=2)
assert_value(True, Solution().canPlaceFlowers, flowerbed=[0, 0], n=1)
assert_value(False, Solution().canPlaceFlowers, flowerbed=[0, 1, 0], n=1)
assert_value(False, Solution().canPlaceFlowers, flowerbed=[1, 0], n=1)
assert_value(True, Solution().canPlaceFlowers, flowerbed=[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0], n=3)
assert_value(True, Solution().canPlaceFlowers, flowerbed=[1, 0, 0, 0, 1], n=1)
assert_value(False, Solution().canPlaceFlowers, flowerbed=[1, 0, 0, 0, 1], n=2)
assert_value(True, Solution().canPlaceFlowers, flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2)
assert_value(True, Solution().canPlaceFlowers, flowerbed=[0, 0, 0, 0], n=1)
assert_value(False, Solution().canPlaceFlowers, flowerbed=[0, 0, 0, 0, 0], n=4)
assert_value(True, Solution().canPlaceFlowers, flowerbed=[1, 0, 0, 0, 1, 0, 0], n=2)
assert_value(True, Solution().canPlaceFlowers, flowerbed=[0, 0, 0, 0, 0, 1, 0, 0], n=0)
assert_value(True, Solution().canPlaceFlowers, flowerbed=[0], n=1)
