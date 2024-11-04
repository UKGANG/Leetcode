'''
523. Continuous Subarray Sum
https://leetcode.com/problems/continuous-subarray-sum/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        cache = {0: -1}
        pre_sum = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            pre_sum %= k
            if pre_sum not in cache:
                cache[pre_sum] = i
                continue
            if i - cache[pre_sum] > 1:
                return True

        return False

    def checkSubarraySum_v0(self, nums: List[int], k: int) -> bool:
        pre_sum = [0]
        for num in nums:
            pre_sum.append(pre_sum[-1] + num)

        pre_sum = [n % k for n in pre_sum]

        cache = {}
        for idx, n in enumerate(pre_sum):
            if n in cache:
                if idx - cache[n] > 1:
                    return True
            else:
                cache[n] = idx

        return False


assert_value(True, Solution().checkSubarraySum, nums=[23, 2, 4, 6, 7], k=6)
assert_value(True, Solution().checkSubarraySum, nums=[23, 2, 6, 4, 7], k=6)
assert_value(False, Solution().checkSubarraySum, nums=[23, 2, 6, 4, 7], k=13)
assert_value(True, Solution().checkSubarraySum, nums=[23, 2, 4, 6, 6], k=7)
assert_value(True, Solution().checkSubarraySum, nums=[2, 4, 3], k=6)
