'''
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)

        dp = [
            [0] * (k << 1) for _ in range(n)
        ]

        for i in range(0, k << 1, 2):
            dp[0][i] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(k << 1):
                if j & 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
                else:
                    dp[i][j] = max(dp[i - 1][j], (dp[i - 1][j - 1] if j else 0) - prices[i])

        return max(dp[-1][i] for i in range(1, k << 1, 2))

    def _maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        k = min(k, n - 1)
        if k < 1:
            return 0
        k <<= 1

        dp_prev = [0] * k
        dp_curr = [0] * k

        for i in range(0, k, 2):
            dp_prev[i] = -prices[0]

        for i in range(1, n):
            for j in range(k):
                dp_curr[j] = max(
                    dp_prev[j],
                    (dp_prev[j - 1] if j > 0 else 0) - prices[i] * ((-1) ** j)
                )

            dp_prev = dp_curr

        return dp_curr[-1]
