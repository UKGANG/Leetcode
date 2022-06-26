'''
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, curr = 0, 0
        for idx in range(1, len(prices)):
            d = prices[idx] - prices[idx - 1]
            curr += d
            curr = max(0, curr)
            res = max(curr, res)
        return res

    def _maxProfit(self, prices: List[int]) -> int:
        res = [0] * len(prices)
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            res[i] = max(0, res[i - 1] + diff, diff)

        return max(res)


assert_value(5, Solution().maxProfit, prices=[7, 1, 5, 3, 6, 4])
assert_value(0, Solution().maxProfit, prices=[7, 6, 4, 3, 1])
