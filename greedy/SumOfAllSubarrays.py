"""
Sum of all Subarrays
https://www.geeksforgeeks.org/sum-of-all-subarrays/
"""
from typing import List
from test_tool import assert_value


class Solution:
    def subarraySum(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for i in range(n):
            res += (i + 1) * (n - i) * arr[i]

        return res

    def _subarraySum_brute_force(self, arr: List[int]) -> int:
        res = 0
        n = len(arr)
        for start in range(n):
            curr = 0
            for end in range(start, n):
                curr += arr[end]
                res += curr
        return res


assert_value(20, Solution().subarraySum, arr=[1, 2, 3])
