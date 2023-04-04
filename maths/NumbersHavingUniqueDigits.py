"""
Numbers having Unique (or Distinct) digits
https://www.geeksforgeeks.org/numbers-unique-distinct-digits/
"""
from test_tool import assert_value


class Solution:
    def uniqueCount(self, start: int, end: int) -> int:
        res = 0
        for n in range(start, end + 1):
            n_str = str(n)
            if len(set(n_str)) == len(n_str):
                res += 1
        return res


assert_value(27, Solution().uniqueCount, start=80, end=120)
