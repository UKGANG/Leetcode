'''
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
from typing import List, Optional

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * len(prices)
        for i in range(1, len(prices)):
            dp[i] = dp[i - 1]
            profit = prices[i] - prices[i - 1]
            dp[i] += max(profit, 0)

        return dp[-1]

    def _dp_maxProfit(self, prices: List[int]) -> int:
        dp_cash = [0] * len(prices)
        dp_stock = [0] * len(prices)

        dp_cash[0] = 0
        dp_stock[0] = -prices[0]

        for i in range(1, len(prices)):
            dp_cash[i] = max(dp_cash[i - 1], dp_stock[i - 1] + prices[i])
            dp_stock[i] = max(dp_stock[i - 1], dp_cash[i - 1] - prices[i])

        return dp_cash[-1]

    def _monostack_decrease_maxProfit(self, prices: List[int]) -> int:
        stack = []
        res = 0
        for p in prices:
            p_prev = p
            while stack and stack[-1] < p:
                p_prev = min(p_prev, stack.pop())
            res += p - p_prev
            stack.append(p)
        return res

    def _monostack_increase_maxProfit(self, prices: List[int]) -> int:
        stack = []
        res = 0
        for sell_price in prices:
            while stack and stack[-1] > sell_price:
                stack.pop()
            if stack:
                res += sell_price - stack[0]
                stack.clear()
            stack.append(sell_price)
        return res

    def _greddy_maxProfit(self, prices: List[int]) -> int:
        res = 0
        for i in range(1, len(prices)):
            profit = prices[i] - prices[i - 1]
            if profit < 0:
                continue
            res += profit

        return res

    def _maxProfit(self, prices: List[int]) -> int:
        diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        diff = [d for d in diff if d > 0]
        return sum(diff)


assert_value(7, Solution().maxProfit, prices=[7, 1, 5, 3, 6, 4])
assert_value(4, Solution().maxProfit, prices=[1, 2, 3, 4, 5])
