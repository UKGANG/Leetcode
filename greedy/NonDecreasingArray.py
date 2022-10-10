'''
665. Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)

        cnt = 0
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                if i == 1 or nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]
                cnt += 1
        return cnt < 2


assert_value(False, Solution().checkPossibility, nums=[4, 2, 1])
assert_value(True, Solution().checkPossibility, nums=[4, 2, 3])
assert_value(True, Solution().checkPossibility, nums=[4, 2, 3])
assert_value(True, Solution().checkPossibility, nums=[1, 4, 2, 3])
assert_value(False, Solution().checkPossibility, nums=[1, 4, 2, 1])
