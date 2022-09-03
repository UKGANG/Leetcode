'''
123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp_prev = [0] * 4
        dp_prev[0] = -prices[0]
        dp_prev[1] = 0
        dp_prev[2] = -prices[0]
        dp_prev[3] = 0
        dp_curr = [0] * 4

        for i in range(1, n):
            dp_curr[0] = max(dp_prev[0], -prices[i])
            dp_curr[1] = max(dp_prev[1], dp_prev[0] + prices[i])
            dp_curr[2] = max(dp_prev[2], dp_prev[1] - prices[i])
            dp_curr[3] = max(dp_prev[3], dp_prev[2] + prices[i])
            dp_prev = dp_curr
        return dp_curr[-1]

    def _maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp = [
            [0] * 4
            for _ in range(n)
        ]
        dp[0][0] = -prices[0]
        dp[0][1] = 0
        dp[0][2] = -prices[0]
        dp[0][3] = 0

        for i in range(1, n):
            dp[i][0] = max(dp[i - 1][0], -prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] - prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] + prices[i])
        return dp[-1][-1]

    def __maxProfit(self, prices: List[int]) -> int:
        res = [0] * len(prices)

        curr_min = prices[0]
        best = 0
        for i in range(len(prices)):
            curr_min = min(curr_min, prices[i])
            best = max(best, prices[i] - curr_min)
            res[i] = best

        curr_max = prices[-1]
        best = 0
        for i in range(len(prices) - 1, -1, -1):
            curr_max = max(curr_max, prices[i])
            best = max(best, curr_max - prices[i])
            res[i] += best

        return max(res)


assert_value(6, Solution().maxProfit, prices=[3, 3, 5, 0, 0, 3, 1, 4])
assert_value(4, Solution().maxProfit, prices=[1, 2, 3, 4, 5])
assert_value(0, Solution().maxProfit, prices=[7, 6, 4, 3, 1])
