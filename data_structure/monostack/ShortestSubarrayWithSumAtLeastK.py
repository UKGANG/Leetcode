'''
862. Shortest Subarray with Sum at Least K
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:

        ...


assert_value(1, Solution().shortestSubarray, nums=[1], k=1)
assert_value(-1, Solution().shortestSubarray, nums=[1, 2], k=4)
assert_value(3, Solution().shortestSubarray, nums=[2, -1, 2], k=3)
