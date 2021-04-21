'''
1033. Moving Stones Until Consecutive
https://leetcode.com/problems/moving-stones-until-consecutive/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        stones = sorted([a, b, c])
        max_cnt = max(stones[1] - stones[0], stones[2] - stones[1]) - 1
        min_cnt = min(stones[1] - stones[0], stones[2] - stones[1]) - 1

        if min_cnt == 0:
            if max_cnt > 0:
                min_cnt = 1
        elif min_cnt == 1:
            max_cnt += 1
        else:
            max_cnt += min_cnt
            min_cnt = 2
        return [min_cnt, max_cnt]


assert_value([1, 2], Solution().numMovesStones, a=1, b=2, c=5)
assert_value([0, 0], Solution().numMovesStones, a=4, b=3, c=2)
assert_value([1, 2], Solution().numMovesStones, a=3, b=5, c=1)
assert_value([1, 1], Solution().numMovesStones, a=2, b=4, c=1)
assert_value([1, 3], Solution().numMovesStones, a=1, b=3, c=6)
assert_value([2, 4], Solution().numMovesStones, a=1, b=4, c=7)
