'''
1526. Minimum Number of Increments on Subarrays to Form a Target Array
https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        pre_sum = [0] * (len(target) + 2)
        for i in range(1, len(target) + 1):
            pre_sum[i] += target[i - 1]
            pre_sum[i + 1] -= target[i - 1]

        return sum([d for d in pre_sum if d > 0])


assert_value(3, Solution().minNumberOperations, target=[1, 2, 3, 2, 1])
assert_value(4, Solution().minNumberOperations, target=[3, 1, 1, 2])
assert_value(7, Solution().minNumberOperations, target=[3, 1, 5, 4, 2])
assert_value(1, Solution().minNumberOperations, target=[1, 1, 1, 1])
assert_value(6, Solution().minNumberOperations, target=[1, 1, 5, 5, 4, 5, 1, 1])
