'''
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
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
