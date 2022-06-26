'''
Coin Sequence
https://algo.monster/problems/amazon_oa_coin_sequence
'''
from collections import Counter
from typing import List

from test_tool import assert_value


class Solution:
    def flips(self, coins: str) -> int:
        coins = coins.lstrip('H')
        coins = coins.lstrip('T')
        cnt = Counter(coins)
        return min(cnt.values())


assert_value(1, Solution().flips, coins='HHTHTT')
