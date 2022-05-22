'''
2178. Maximum Split of Positive Even Integers
https://leetcode.com/problems/maximum-split-of-positive-even-integers/
'''
import math
from typing import List

from test_tool import assert_value


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        n = math.sqrt(.25 + finalSum) - .5
        n = math.ceil(n)
        res = list(range(2, (n + 1) << 1, 2))
        total = ((res[0] + res[-1]) * n) >> 1
        diff = total - finalSum
        if diff:
            del res[(diff >> 1) - 1]

        return res

    def _maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1:
            return []
        finalSum >>= 1
        finalSum -= 1
        res = [1]
        while finalSum > 0:
            res.append(res[-1] + 1)
            finalSum -= res[-1]
            if finalSum < 0:
                del res[-finalSum - 1]

        return [i << 1 for i in res]


assert_value([2, 4, 6], Solution().maximumEvenSplit, finalSum=12)
assert_value([], Solution().maximumEvenSplit, finalSum=7)
assert_value([4, 6, 8, 10], Solution().maximumEvenSplit, finalSum=28)
assert_value([2, 4, 6, 8, 10, 12, 16, 18, 20], Solution().maximumEvenSplit, finalSum=96)
