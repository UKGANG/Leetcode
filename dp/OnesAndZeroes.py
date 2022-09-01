'''
474. Ones and Zeroes
https://leetcode.com/problems/ones-and-zeroes/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        for s in strs:
            zero = s.count('0')
            one = s.count('1')
            for j in range(m, zero - 1, -1):
                for k in range(n, one - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - zero][k - one] + 1)
        return dp[-1][-1]


assert_value(4, Solution().findMaxForm, strs=["10", "0001", "111001", "1", "0"], m=5, n=3)
assert_value(2, Solution().findMaxForm, strs=["10", "0", "1"], m=1, n=1)
assert_value(3, Solution().findMaxForm, strs=["10", "0001", "111001", "1", "0"], m=3, n=4)
