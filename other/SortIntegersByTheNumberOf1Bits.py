"""
1356. Sort Integers by The Number of 1 Bits
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""
from collections import Counter
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

    def _sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (Counter(bin(x)[2:])['1'], x))

    def __sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (sum(int(y) for y in list(bin(x)[2:])), x))
