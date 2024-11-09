"""
219. Contains Duplicate II
https://leetcode.com/problems/contains-duplicate-ii/
"""
import bisect
import heapq
import operator
from typing import List

from test_tool import assert_value


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}
        for idx, n in enumerate(nums):
            if idx - cache.get(n, -k - 1) <= k:
                return True
            cache[n] = idx
        return False
