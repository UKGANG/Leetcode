'''
123. Best Time to Buy and Sell Stock III
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
