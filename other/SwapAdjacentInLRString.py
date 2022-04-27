'''
777. Swap Adjacent in LR String
https://leetcode.com/problems/swap-adjacent-in-lr-string/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.replace('X', '') != end.replace('X', ''):
            return False
        l_start = [idx for idx, c in enumerate(start) if c == 'L']
        r_start = [idx for idx, c in enumerate(start) if c == 'R']
        l_end = [idx for idx, c in enumerate(end) if c == 'L']
        r_end = [idx for idx, c in enumerate(end) if c == 'R']

        for idx_start, idx_end in zip(l_start, l_end):
            if idx_start < idx_end:
                return False
        for idx_start, idx_end in zip(r_start, r_end):
            if idx_start > idx_end:
                return False

        return True


assert_value(True, Solution().canTransform, start="RXXLRXRXL", end="XRLXXRRLX")
assert_value(False, Solution().canTransform, start="X", end="L")
assert_value(False, Solution().canTransform, start="LXXLXRLXXL", end="XLLXRXLXLX")
