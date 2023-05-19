"""
658. Find K Closest Elements
https://leetcode.com/problems/find-k-closest-elements
"""
import bisect
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        right = bisect.bisect(arr, x)
        left = right - 1

        while right - left - 1 < k:
            if left == -1:
                right += 1
                continue
            if right == len(arr):
                left -= 1
                continue
            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        return arr[left + 1: right]
