"""
1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number
"""
import itertools
from collections import deque
from typing import List, Dict, Tuple

from test_tool import assert_value


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) >> 1
            if arr[m] - m - 1 < k:
                l = m + 1
            else:
                r = m

        return l + k

    def findKthPositive_brute_force(self, arr: List[int], k: int) -> int:
        arr = deque(arr)
        last = None
        for i in range(1, arr[-1] + 1):
            if i == arr[0]:
                last = arr.popleft()
            else:
                k -= 1
            if not k:
                return i
        return last + k
