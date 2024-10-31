'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, res = float('inf'), 0
        for price in prices:
            min_price = min(min_price, price)
            res = max(res, price - min_price)
        return res

    def maxProfit_v3(self, prices: List[int]) -> int:
        res, curr = 0, 0
        for idx in range(1, len(prices)):
            d = prices[idx] - prices[idx - 1]
            curr += d
            curr = max(0, curr)
            res = max(curr, res)
        return res

    def maxProfit_v2(self, prices: List[int]) -> int:
        dp_cash = [0] * len(prices)
        dp_stock = [0] * len(prices)

        dp_cash[0] = 0
        dp_stock[0] = -prices[0]

        for i in range(1, len(prices)):
            dp_cash[i] = max(dp_cash[i - 1], dp_stock[i - 1] + prices[i])
            dp_stock[i] = max(dp_stock[i - 1], -prices[i])

        return dp_cash[-1]

    def maxProfit_v1(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1:
            return 0

        diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]

        dp = [0] * len(diff)

        dp[0] = diff[0]

        for i in range(1, len(diff)):
            dp[i] = max(dp[i - 1] + diff[i], diff[i], 0)

        return max(*dp, 0)

    def maxProfit_v0(self, prices: List[int]) -> int:
        res = [0] * len(prices)
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            res[i] = max(0, res[i - 1] + diff, diff)

        return max(res)


assert_value(5, Solution().maxProfit, prices=[7, 1, 5, 3, 6, 4])
assert_value(0, Solution().maxProfit, prices=[7, 6, 4, 3, 1])
