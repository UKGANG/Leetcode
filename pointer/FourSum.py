'''
18. 4Sum
https://leetcode.com/problems/4sum/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for a in range(len(nums) - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums) - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue
                target_s = target - nums[a] - nums[b]
                c, d = b + 1, len(nums) - 1
                while c < d:
                    s = nums[c] + nums[d]
                    if s == target_s:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif s > target_s:
                        d -= 1
                    else:
                        c += 1
        return res


assert_value([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], Solution().fourSum, nums=[1, 0, -1, 0, -2, 2], target=0)
assert_value([[2, 2, 2, 2]], Solution().fourSum, nums=[2, 2, 2, 2, 2], target=8)
assert_value([[-2, -1, 1, 2], [-1, -1, 1, 1]], Solution().fourSum, nums=[-2, -1, -1, 1, 1, 2, 2], target=0)
