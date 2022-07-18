'''
2272. Substring With Largest Variance
https://leetcode.com/problems/substring-with-largest-variance/
'''
import collections
from operator import itemgetter
from typing import List, Optional, Tuple

from test_tool import assert_value


class Solution:
    def largestVariance(self, s: str) -> int:
        ...


assert_value(3, Solution().largestVariance, s = "aababbb")
assert_value(0, Solution().largestVariance, s = "abcde")