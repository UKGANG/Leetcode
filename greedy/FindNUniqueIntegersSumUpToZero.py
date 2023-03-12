"""
1304. Find N Unique Integers Sum up to Zero
https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = list(range(1, n))
        res.append(-(n * (n - 1)) >> 1)
        return res
