"""

"""
import operator
from typing import List

from test_tool import assert_value


class Solution:
    def accommodate(self, ids: List[int], prices: List[int], guests: List[int], target: int) -> int:
        dp = [
            [float('inf'), []]
            for _ in range(target + 1)
         ]
        dp[0][0] = 0

        for i in range(len(ids)):
            hotel_id = ids[i]
            price = prices[i]
            guest = guests[i]
            for j in range(target, guest - 1, -1):
                if dp[j - guest][0] == float('inf') or dp[j - guest][0] + price > dp[j][0]:
                    continue
                dp[j][0] = dp[j - guest][0] + price
                dp[j][1].clear()
                dp[j][1].extend(dp[j - guest][1])
                dp[j][1].append(hotel_id)
        return max(dp, key=operator.itemgetter(0))[1]


assert_value(
    [3, 4], Solution().accommodate,
    ids=[1, 2, 3, 4], prices=[180, 280, 220, 310], guests=[1, 2, 2, 3], target=5)
