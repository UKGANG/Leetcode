"""
873. Length of Longest Fibonacci Subsequence
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence
"""
import collections
from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_idx = {n: idx for idx, n in enumerate(arr)}
        dp = collections.defaultdict(lambda: 2)

        res = 0
        for j in range(2, len(arr)):
            for k in range(1, j):
                i = arr_idx.get(arr[j] - arr[k], None)
                if i is None:
                    continue
                if i >= k:
                    continue
                dp[k, j] = dp[i, k] + 1
                res = max(res, dp[k, j])
        return res if res >= 3 else 0
