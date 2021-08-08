'''
713. Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        p = 1
        res = 0
        l, r = 0, 0
        while r < len(nums):
            p *= nums[r]
            while p >= k and l <= r:
                p /= nums[l]
                l += 1
            res += r - l + 1
            r += 1

        return res


assert_value(8, Solution().numSubarrayProductLessThanK, nums=[10, 5, 2, 6], k=100)
assert_value(0, Solution().numSubarrayProductLessThanK, nums=[1, 2, 3], k=0)
assert_value(25, Solution().numSubarrayProductLessThanK, nums=[10, 5, 2, 6, 3, 4, 1, 4, 9], k=100)
