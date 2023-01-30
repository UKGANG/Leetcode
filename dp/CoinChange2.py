'''
518. Coin Change 2
https://leetcode.com/problems/coin-change-2/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for sub_total in range(coin, amount + 1):
                dp[sub_total] += dp[sub_total - coin]
        return dp[-1]

    def _change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount

        dp = [0] * (n + 1)

        dp[0] = 1

        for i in range(m):
            for j in range(coins[i], n + 1):
                dp[j] += dp[j - coins[i]]
        return dp[-1]

    def __change(self, amount: int, coins: List[int]) -> int:
        m, n = len(coins), amount

        dp = [
            [0] * (n + 1)
            for _ in range(m)
        ]

        for i in range(m):
            dp[i][0] = 1

        for i in range(coins[0], n + 1):
            dp[0][i] += dp[0][i - coins[0]]

        for i in range(1, m):
            for j in range(1, n + 1):
                dp[i][j] += dp[i - 1][j]
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j - coins[i]]
        return dp[-1][-1]
