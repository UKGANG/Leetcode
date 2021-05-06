'''
46. Permutations
https://leetcode.com/problems/permutations/
'''
import re
from typing import List

from test_tool import assert_value


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums]
        for idx, num in enumerate(nums):
            for p in self.permute(nums[:idx] + nums[idx + 1:]):
                result.append([num] + p)

        return result


assert_value([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], Solution().permute, nums=[1, 2, 3])
