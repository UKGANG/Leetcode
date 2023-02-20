"""
370. Range Addition
https://leetcode.com/problems/range-addition/description/
"""
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * (length + 1)
        for start, end, val in updates:
            res[start] += val
            res[end + 1] -= val
        for i in range(len(res) - 1):
            res[i + 1] += res[i]

        return res[:-1]
