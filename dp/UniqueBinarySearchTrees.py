'''
96. Unique Binary Search Trees
https://leetcode.com/problems/unique-binary-search-trees/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[i - j - 1] * dp[j]
        return dp[-1]

    def _numTrees(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):

            for j in range(i >> 1):
                left = dp[j]
                right = dp[i - 1 - j]
                dp[i] += (left * right) << 1
            if i & 1:
                dp[i] += dp[i >> 1] ** 2

        return dp[-1]

    def __numTrees(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        for i in range(3, n + 1):
            for j in range(i):
                left = dp[j]
                right = dp[i - 1 - j]
                dp[i] += (left * right)

        return dp[-1]
