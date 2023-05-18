"""
697. Degree of an Array
https://leetcode.com/problems/degree-of-an-array
"""
import collections
from typing import List


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        max_key, max_val = [], 0
        for k, v in counter.items():
            if v > max_val:
                max_key, max_val = [k], v
            elif v == max_val:
                max_key.append(k)
        key_len = {k: [len(nums), 0] for k in max_key}
        for idx, n in enumerate(nums):
            if n in key_len:
                key_len[n][0], key_len[n][1] = min(key_len[n][0], idx), max(key_len[n][1], idx)

        res = [0, len(nums)]
        for key, (left, right) in key_len.items():
            if right - left < res[1] - res[0]:
                res[0], res[1] = left, right
        return res[1] - res[0] + 1
