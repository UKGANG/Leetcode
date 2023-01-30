'''
322. Coin Change
https://leetcode.com/problems/coin-change/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        coins.sort()
        for sub_total in range(amount + 1):
            for coin in coins:
                if coin > sub_total:
                    break
                dp[sub_total] = min(dp[sub_total], dp[sub_total - coin] + 1)
        return -1 if dp[-1] == float('inf') else dp[sub_total]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        m, n = len(coins), amount

        dp = [float('inf')] * (n + 1)

        dp[0] = 0
        for i in range(m):
            if coins[i] > amount:
                continue
            for j in range(coins[i], n + 1):
                if dp[j - coins[i]] != float('inf'):
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)

        return -1 if dp[-1] == float('inf') else dp[-1]

    def _coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        m, n = len(coins), amount

        dp = [0] * (n + 1)

        for i in range(m):
            if coins[i] > amount:
                continue
            dp[coins[i]] = 1
            for j in range(coins[i] + 1, n + 1):
                if dp[j - coins[i]]:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1) if dp[j] else dp[j - coins[i]] + 1

        return dp[-1] if dp[-1] else -1

    def __coinChange(self, coins: List[int], amount: int) -> int:
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
