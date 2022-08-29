'''
343. Integer Break
https://leetcode.com/problems/integer-break/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def integerBreak(self, n: int) -> int:
        if n < 3:
            return 1
        dp = [1] * (n + 1)
        for i in range(3, n + 1):
            for j in range(1, i - 1):
                dp[i] = max(dp[i], dp[i - j] * j, (i - j) * j)
        return dp[-1]
