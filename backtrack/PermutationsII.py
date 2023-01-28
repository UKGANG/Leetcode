'''
47. Permutations II
https://leetcode.com/problems/permutations-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack():
            if len(combo) == len(nums):
                res.append(combo[:])
                return
            seen_curr = set()
            for i in range(len(nums)):
                if seen[i]:
                    continue
                if nums[i] in seen_curr:
                    continue
                seen_curr.add(nums[i])
                seen[i] = True
                combo.append(nums[i])
                backtrack()
                combo.pop()
                seen[i] = False
        res, combo, seen = [], [], [False] * len(nums)
        backtrack()
        return res

    def _permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]

        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums]
            return [nums, nums[::-1]]

        num = nums[0]

        res = []
        ps = self._permuteUnique(nums[1:])
        for p in ps:
            for i in range(len(nums)):
                res.append(p[:i] + [num] + p[i:])
                if i < len(p) and p[i] == num:
                    break
        return sorted(res)


# assert_value([[]], Solution().permuteUnique, nums=[])
#
# assert_value([[1]], Solution().permuteUnique, nums=[1])

assert_value([[1, 1, 2],
              [1, 2, 1],
              [2, 1, 1]], Solution().permuteUnique, nums=[1, 1, 2])

# assert_value([[1, 2, 3],
#               [1, 3, 2],
#               [2, 1, 3],
#               [2, 3, 1],
#               [3, 1, 2],
#               [3, 2, 1]], Solution().permuteUnique,
#              nums=[1, 2, 3])
