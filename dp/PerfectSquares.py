'''
279. Perfect Squares
https://leetcode.com/problems/perfect-squares/
'''
import collections
import math
from typing import List

from test_tool import assert_value


class Solution:
    def numSquares(self, n: int) -> int:
        curr_level = collections.deque([0])
        res = 0
        visited = set([0])
        while curr_level:
            size = len(curr_level)
            res += 1
            for _ in range(size):
                curr = curr_level.popleft()
                for i in range(int(math.sqrt(n - curr)), 0, -1):
                    next_val = curr + i ** 2
                    if next_val == n:
                        return res
                    if next_val in visited:
                        continue
                    visited.add(next_val)
                    curr_level.append(curr + i ** 2)

        return 0

    def _numSquares(self, n: int) -> int:
        m, n = int(math.sqrt(n)), n

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, m + 1):
            i *= i
            for j in range(i, n + 1):
                if dp[j - i] == float('inf'):
                    continue
                dp[j] = min(dp[j], dp[j - i] + 1)
        return 0 if dp[-1] == float('inf') else dp[-1]
