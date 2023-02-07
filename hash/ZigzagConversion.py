"""
6. Zigzag Conversion
https://leetcode.com/problems/zigzag-conversion/description/
"""
import math

from test_tool import assert_value


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        m = (numRows << 1) - 2

        s_with_hash = []
        for i in range(len(s)):
            row_hash = i % m
            col_hash = i // m * (numRows - 1)

            if row_hash >= numRows:
                col_hash += row_hash - numRows + 1
                row_hash = (numRows << 1) - row_hash - 2
            row_hash = math.ceil(len(s) / m) * row_hash
            s_with_hash.append((row_hash * m + col_hash, s[i]))

        return ''.join(c for hashcode, c in sorted(s_with_hash))


assert_value('PAHNAPLSIIGYIR', Solution().convert, s='PAYPALISHIRING', numRows=3)
assert_value('PINALSIGYAHRPI', Solution().convert, s='PAYPALISHIRING', numRows=4)
assert_value('A', Solution().convert, s='A', numRows=1)
