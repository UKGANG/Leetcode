'''
611. Valid Triangle Number
https://leetcode.com/problems/valid-triangle-number/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        nums = sorted(nums)

        for k in range(2, len(nums)):
            i, j = 0, k - 1
            while i < j:
                if nums[i] + nums[j] <= nums[k]:
                    i += 1
                else:
                    res += j - i
                    j -= 1

        return res


assert_value(3, Solution().triangleNumber, nums=[2, 2, 3, 4])
assert_value(4, Solution().triangleNumber, nums=[4, 2, 3, 4])
assert_value(0, Solution().triangleNumber, nums=[1, 1, 3, 4])
assert_value(0, Solution().triangleNumber, nums=[7, 0, 0, 0])
