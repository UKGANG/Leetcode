'''
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''
import re
from typing import List

from test_tool import assert_value


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
                continue
            nums[abs(num) - 1] *= -1
        return result


assert_value([2, 3], Solution().findDuplicates, nums=[4, 3, 2, 7, 8, 2, 3, 1])
assert_value([1], Solution().findDuplicates, nums=[1, 1, 2])
assert_value([], Solution().findDuplicates, nums=[1])
