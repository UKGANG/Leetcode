'''
714. Best Time to Buy and Sell Stock with Transaction Fee
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
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

    def _dp_maxProfit(self, prices: List[int], fee: int) -> int:
        hold_stock = [0] * len(prices)
        hold_money = [0] * len(prices)
        hold_stock[0] = -prices[0]
        for i in range(1, len(prices)):
            hold_stock[i] = max(hold_stock[i - 1], hold_money[i - 1] - prices[i])
            hold_money[i] = max(hold_money[i - 1], hold_stock[i - 1] + prices[i] - fee)
        return hold_money[-1]
