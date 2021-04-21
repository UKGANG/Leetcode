'''
1189. Maximum Number of Balloons
https://leetcode.com/problems/maximum-number-of-balloons/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cache = {}
        for c in text:
            cache[c] = cache[c] + 1 if c in cache else 1
        cache = {k: v for k, v in cache.items() if k in "balon"}
        ban = [v for k, v in cache.items() if k in "ban"]
        lo = [v for k, v in cache.items() if k in "lo"]
        ban = 0 if len(ban) == 0 else min(ban)
        lo = 0 if len(lo) == 0 else min(lo)
        if ban * 2 > lo:
            return int(lo / 2)
        else:
            return ban


assert_value(1, Solution().maxNumberOfBalloons, text="nlaebolko")
assert_value(2, Solution().maxNumberOfBalloons, text="loonbalxballpoon")
assert_value(0, Solution().maxNumberOfBalloons, text="leetcode")
