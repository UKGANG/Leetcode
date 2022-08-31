'''
1049. Last Stone Weight II
https://leetcode.com/problems/last-stone-weight-ii/
'''
import itertools
from typing import List

from test_tool import assert_value


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones.sort()
        m, n = len(stones), sum(stones) >> 1
        dp = [False] * (n + 1)

        dp[0] = True
        dp[stones[0]] = True

        max_res = stones[0]
        for i in range(1, m):
            for j in range(n, stones[i] - 1, -1):
                dp[j] = dp[j] or dp[j - stones[i]]
                if dp[j]:
                    max_res = max(max_res, j)

        return sum(stones) - (max_res << 1)


assert_value(91, Solution().lastStoneWeightII, stones=[91])
assert_value(0, Solution().lastStoneWeightII, stones=[1, 1, 4, 2, 2])
assert_value(1, Solution().lastStoneWeightII, stones=[1, 2])
assert_value(1, Solution().lastStoneWeightII, stones=[2, 7, 4, 1, 8, 1])
assert_value(5, Solution().lastStoneWeightII, stones=[31, 26, 33, 21, 40])
