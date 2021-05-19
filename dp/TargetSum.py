'''
494. Target Sum
https://leetcode.com/problems/target-sum/
'''
from collections import Counter
from typing import List

from test_tool import assert_value


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        dic = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdic = {}
            for d in dic:
                tdic[d + nums[i]] = tdic.get(d + nums[i], 0) + dic[d]
                tdic[d - nums[i]] = tdic.get(d - nums[i], 0) + dic[d]
            dic = tdic
        return dic.get(target, 0)


assert_value(5, Solution().findTargetSumWays, nums=[1, 1, 1, 1, 1], target=3)
assert_value(1, Solution().findTargetSumWays, nums=[1], target=1)
