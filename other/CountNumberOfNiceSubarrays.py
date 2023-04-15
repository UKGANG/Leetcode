"""
1248. Count Number of Nice Subarrays
https://leetcode.com/problems/count-number-of-nice-subarrays
"""
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most_k(k):
            start = 0
            res = 0
            for end in range(len(nums)):
                if nums[end] & 1:
                    k -= 1
                while k < 0:
                    if nums[start] & 1:
                        k += 1
                    start += 1
                res += end - start + 1
            return res

        return at_most_k(k) - at_most_k(k - 1)
