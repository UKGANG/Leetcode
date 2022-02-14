'''
1010. Pairs of Songs With Total Durations Divisible by 60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        cnt = collections.Counter(time)
        cnt_30 = (cnt[30] * (cnt[30] - 1)) >> 1
        cnt_60 = (cnt[0] * (cnt[0] - 1)) >> 1
        del cnt[30]
        del cnt[60]
        res = cnt_30 + cnt_60
        for i in range(30):
            res += cnt[i] * cnt[60 - i]
        return res


assert_value(3, Solution().numPairsDivisibleBy60, time=[30, 20, 150, 100, 40])
assert_value(3, Solution().numPairsDivisibleBy60, time=[60, 60, 60])
