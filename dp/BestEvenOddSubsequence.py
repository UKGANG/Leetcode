from typing import List
from collections import defaultdict

from test_tool import assert_value


class Solution:
    def bestEvenOddSubsequence(self, arr: List[int]) -> int:
        sum_odd = []
        sum_even = []
        for i in arr:
            if self.is_odd(i):
                prev_sum = 0 if len(sum_even) == 0 else max(sum_even)
                sum_odd.append(prev_sum + i)
            else:
                prev_sum = 0 if len(sum_odd) == 0 else max(sum_odd)
                sum_even.append(prev_sum + i)

        return max(sum_odd[-1:] + sum_even[-1:])

    def is_odd(self, i: int) -> bool:
        return bool(i & 1)


assert_value(15, Solution().bestEvenOddSubsequence, arr=[1, 2, 3, 4, 5])
assert_value(5, Solution().bestEvenOddSubsequence, arr=[2, -2, 1, 3])
