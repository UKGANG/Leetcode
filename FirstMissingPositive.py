"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive
"""
from typing import List


class Solution:
    def _elegant_firstMissingPositive(self, nums: List[int]) -> int:
        nums.insert(0, 0)
        n = len(nums)

        for i in range(n):
            if not 0 < nums[i] < n:
                nums[i] = 0

        for i in range(n):
            nums[nums[i] % n] += n

        for i in range(n):
            if not divmod(nums[i], n)[0]:
                return i

        return n

    def _inplace_firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        if 1 not in nums:
            return 1
        for i in range(n):
            if not 0 < nums[i] < n + 1:
                nums[i] = 1
        for i in range(n):
            nums[abs(nums[i]) - 1] = -abs(nums[abs(nums[i]) - 1])

        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1

    def _naive_firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * n
        for i in range(n):
            if not 0 < nums[i] < n + 1:
                continue
            seen[nums[i] - 1] = True
        for i in range(n):
            if not seen[i]:
                return i + 1
        return n + 1
