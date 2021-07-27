'''
992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMostK(nums, k) - self.atMostK(nums, k - 1)

    def atMostK(self, nums: List[int], k: int):
        cache = {}
        i = 0
        res = 0
        for j in range(len(nums)):
            if nums[j] not in cache:
                cache[nums[j]] = 1
                k -= 1
            else:
                cache[nums[j]] += 1
            while k < 0:
                cache[nums[i]] -= 1
                if cache[nums[i]] == 0:
                    del cache[nums[i]]
                    k += 1
                i += 1
            res += j - i + 1
        return res


assert_value(7, Solution().subarraysWithKDistinct, nums=[1, 2, 1, 2, 3], k=2)
assert_value(3, Solution().subarraysWithKDistinct, nums=[1, 2, 1, 3, 4], k=3)
