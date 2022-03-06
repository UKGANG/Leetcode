'''
122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
from typing import List, Optional

from test_tool import assert_value


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        diff = [d for d in diff if d > 0]
        return sum(diff)


assert_value(7, Solution().maxProfit, prices=[7, 1, 5, 3, 6, 4])
assert_value(4, Solution().maxProfit, prices=[1, 2, 3, 4, 5])
