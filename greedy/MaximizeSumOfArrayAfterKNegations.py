'''
1005. Maximize Sum Of Array After K Negations
https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/
'''
import heapq
from typing import List

from test_tool import assert_value


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=abs, reverse=True)
        for i in range(len(nums)):
            if nums[i] >= 0:
                continue
            if not k:
                break
            nums[i] *= -1
            k -= 1

        if k & 1:
            nums[-1] *= -1
        return sum(nums)

    def _largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k:
            curr = heapq.heappop(nums)
            heapq.heappush(nums, -curr)
            k -= 1

        return sum(nums)
