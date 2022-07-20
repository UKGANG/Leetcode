'''
27. Remove Element
https://leetcode.com/problems/remove-element/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        f, s = 0, 0

        while f < len(nums):
            if nums[f] != val:
                nums[s], nums[f] == nums[f], nums[s]
                s += 1
            f += 1
        return s

    def _removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums) - 1
        res = 0
        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                res += 1
            else:
                l += 1
        return len(nums) - res


assert_value(2, Solution().removeElement, nums=[3, 2, 2, 3], val=3)
assert_value(5, Solution().removeElement, nums=[0, 1, 2, 2, 3, 0, 4, 2], val=2)
assert_value(0, Solution().removeElement, nums=[1], val=1)
