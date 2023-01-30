'''
309. Best Time to Buy and Sell Stock with Cooldown
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp_buyable = [0] * n
        dp_frozen = [0] * n
        dp_sellable = [0] * n

        dp_sellable[0] = -prices[0]

        for i in range(1, n):
            dp_buyable[i] = max(dp_buyable[i - 1], dp_frozen[i - 1])
            dp_frozen[i] = dp_sellable[i - 1] + prices[i]
            dp_sellable[i] = max(dp_sellable[i - 1], dp_buyable[i - 1] - prices[i])

        return max(dp_buyable[-1], dp_frozen[-1])

    def _maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        dp_sell = [0] * n
        dp_buy = [0] * n

        dp_sell[0] = 0
        dp_buy[0] = -prices[0]

        for i in range(1, n):
            dp_sell[i] = max(dp_sell[i - 1], dp_buy[i - 1] + prices[i])
            dp_buy[i] = max(dp_buy[i - 1], (dp_sell[i - 2] if i > 1 else 0) - prices[i])
        return dp_sell[-1]

    def __maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        dp_hold_stock = [0] * n
        dp_sold = [0] * n
        dp_frozen = [0] * n
        dp_buyable = [0] * n

        dp_hold_stock[0] = -prices[0]
        dp_sold[0] = 0
        dp_frozen[0] = 0
        dp_buyable[0] = 0

        for i in range(1, n):
            dp_hold_stock[i] = max(dp_hold_stock[i - 1], dp_buyable[i - 1] - prices[i], dp_frozen[i - 1] - prices[i])
            dp_sold[i] = dp_hold_stock[i - 1] + prices[i]
            dp_frozen[i] = dp_sold[i - 1]
            dp_buyable[i] = max(dp_buyable[i - 1], dp_frozen[i - 1])

        return max(dp_sold[-1], dp_frozen[-1], dp_buyable[-1])

    def ___maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        dp_sell = [0] * n
        dp_frozen = [0] * n
        dp_buy = [0] * n

        dp_sell[0] = 0
        dp_frozen[0] = 0
        dp_buy[0] = -prices[0]

        dp_sell[1] = max(dp_sell[0], dp_buy[0] + prices[1])
        dp_frozen[1] = 0
        dp_buy[1] = max(dp_buy[0], dp_frozen[0] - prices[1])

        for i in range(2, n):
            dp_sell[i] = max(dp_sell[i - 1], dp_buy[i - 1] + prices[i])
            dp_frozen[i] = dp_sell[i - 1]
            dp_buy[i] = max(dp_buy[i - 1], dp_frozen[i - 1] - prices[i], max(dp_sell[:i - 1]) - prices[i])
        return dp_sell[-1]

    def ____maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        dp_sell = [0] * n
        dp_buy = [0] * n

        dp_sell[0] = 0
        dp_buy[0] = -prices[0]

        dp_sell[1] = max(dp_sell[0], dp_buy[0] + prices[1])
        dp_buy[1] = -prices[1]

        for i in range(2, n):
            dp_sell[i] = max(dp_sell[i - 1], dp_buy[i - 1] + prices[i])
            dp_buy[i] = max(dp_buy[i - 1], dp_sell[i - 2] - prices[i])
        return dp_sell[-1]
