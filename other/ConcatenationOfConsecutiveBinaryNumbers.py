'''
1680. Concatenation of Consecutive Binary Numbers
https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        l, ans = 0, 0
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                l += 1
            ans = ((ans << l) | i) % (10 ** 9 + 7)
        return (ans)


assert_value(1, Solution().concatenatedBinary, n=1)
assert_value(27, Solution().concatenatedBinary, n=3)
assert_value(505379714, Solution().concatenatedBinary, n=12)
