'''
47. Permutations II
https://leetcode.com/problems/permutations/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def _permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = set()
        if len(nums) == 1:
            return [nums]
        for idx, num in enumerate(nums):
            for p in self.permuteUnique(nums[:idx] + nums[idx + 1:]):
                result.add(tuple([num] + list(p)))

        return sorted([list(p) for p in result])

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums]
            return [nums, nums[::-1]]

        num = nums[0]

        res = []
        ps = self.permuteUnique(nums[1:])
        for p in ps:
            for i in range(len(nums)):
                res.append(p[:i] + [num] + p[i:])
                if i < len(p) and p[i] == num:
                    break
        return sorted(res)


assert_value([[]], Solution().permuteUnique, nums=[])

assert_value([[1]], Solution().permuteUnique, nums=[1])

assert_value([[1, 1, 2],
              [1, 2, 1],
              [2, 1, 1]], Solution().permuteUnique, nums=[1, 1, 2])

assert_value([[1, 2, 3],
              [1, 3, 2],
              [2, 1, 3],
              [2, 3, 1],
              [3, 1, 2],
              [3, 2, 1]], Solution().permuteUnique,
             nums=[1, 2, 3])
