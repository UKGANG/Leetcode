'''
322. Coin Change
https://leetcode.com/problems/coin-change/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin < 0:
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[-1] == float('inf'):
            return -1
        return dp[-1]


assert_value(3, Solution().coinChange, coins=[1, 2, 5], amount=11)
assert_value(-1, Solution().coinChange, coins=[2], amount=3)
assert_value(0, Solution().coinChange, coins=[1], amount=0)
