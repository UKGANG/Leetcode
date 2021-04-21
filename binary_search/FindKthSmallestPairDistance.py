'''
719. Find K-th Smallest Pair Distance
https://leetcode.com/problems/find-k-th-smallest-pair-distance/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)

        lo = 0
        hi = nums[-1] - nums[0]

        while lo < hi:
            guess = (lo + hi) // 2
            if self.shift_right(nums, guess, k):
                lo = guess + 1
            else:
                hi = guess
        return hi

    def shift_right(self, nums, guess, k):
        i = 0
        j = 1
        cnt = 0
        while i < len(nums):
            while j < len(nums) and nums[j] - nums[i] <= guess:
                j += 1
            cnt += j - i - 1
            i += 1
        return cnt < k


assert_value(0, Solution().smallestDistancePair, nums=[1, 3, 1], k=1)
assert_value(5, Solution().smallestDistancePair, nums=[1, 6, 1], k=3)
assert_value(2, Solution().smallestDistancePair, nums=[9, 10, 7, 10, 6, 1, 5, 4, 9, 8], k=18)
