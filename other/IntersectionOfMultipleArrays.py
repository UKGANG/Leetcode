"""
2248. Intersection of Multiple Arrays
https://leetcode.com/problems/intersection-of-multiple-arrays
"""
import collections
import operator
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        nums = sum(nums, [])
        res = filter(lambda item: item[1] >= n, collections.Counter(nums).items())
        res = map(operator.itemgetter(0), res)
        return sorted(res)
