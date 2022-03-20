'''
560. Subarray Sum Equals K
https://leetcode.com/problems/subarray-sum-equals-k/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre_sum = {0: 1}
        curr = 0
        res = 0
        for num in nums:
            curr += num
            res += pre_sum.get(curr - k, 0)
            pre_sum[curr] = pre_sum.get(curr, 0) + 1
        return res


assert_value(2, Solution().subarraySum, nums=[1, 1, 1], k=2)
assert_value(2, Solution().subarraySum, nums=[1, 2, 3], k=3)
assert_value(0, Solution().subarraySum, nums=[1], k=0)
assert_value(1, Solution().subarraySum, nums=[0], k=0)
