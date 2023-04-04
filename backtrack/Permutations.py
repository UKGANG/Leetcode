'''
46. Permutations
https://leetcode.com/problems/permutations/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(combo) == len(nums):
                res.append(combo[:])
                return
            for num in nums:
                if num in seen:
                    continue
                seen.add(num)
                combo.append(num)
                backtrack()
                combo.pop()
                seen.remove(num)

        res, combo, seen = [], [], set()
        backtrack()
        return res

    def _permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums]
        for idx, num in enumerate(nums):
            for p in self._permute(nums[:idx] + nums[idx + 1:]):
                result.append([num] + p)

        return result


assert_value([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]], Solution().permute, nums=[1, 2, 3])
assert_value([[1, 2], [2, 1]], Solution().permute, nums=[1, 2])
