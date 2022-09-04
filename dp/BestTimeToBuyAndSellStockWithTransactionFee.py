'''
714. Best Time to Buy and Sell Stock with Transaction Fee
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)

        dp_hold_stock = [0] * n
        dp_hold_cache = [0] * n

        dp_hold_stock[0] = -prices[0]
        dp_hold_cache[0] = 0

        for i in range(1, n):
            dp_hold_stock[i] = max(dp_hold_stock[i - 1], dp_hold_cache[i - 1] - prices[i])
            dp_hold_cache[i] = max(dp_hold_cache[i - 1], dp_hold_stock[i - 1] + prices[i] - fee)

        return dp_hold_cache[-1]

    def _greedy_maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) < 2:
            return 0
        res = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]

            if prices[i] - buy <= fee:
                continue

            res += prices[i] - buy - fee
            buy = prices[i] - fee

        return res
