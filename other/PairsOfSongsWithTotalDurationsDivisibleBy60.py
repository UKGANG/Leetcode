'''
1010. Pairs of Songs With Total Durations Divisible by 60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cache = {}
        for song in time:
            song %= 60
            cache[song] = cache.get(song, 0)
            cache[song] += 1

        res = 0
        for i in range(1, 30):
            res += cache.get(i, 0) * cache.get(60 - i, 0)

        for i in [0, 30]:
            if cache.get(i, 0) > 1:
                res += ((cache[i] * (cache[i] - 1)) >> 1)

        return res

    def _numPairsDivisibleBy60(self, time: List[int]) -> int:
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


# assert_value(3, Solution().numPairsDivisibleBy60, time=[30, 20, 150, 100, 40])
# assert_value(3, Solution().numPairsDivisibleBy60, time=[60, 60, 60])
assert_value(1, Solution().numPairsDivisibleBy60, time=[451, 209])
# assert_value(1, Solution().numPairsDivisibleBy60, time=[15,63,451,213,37,209,343,319])
