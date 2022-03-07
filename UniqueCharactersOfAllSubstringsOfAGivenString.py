'''
828. Count Unique Characters of All Substrings of a Given String
https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
'''
from collections import defaultdict
from typing import List

from test_tool import assert_value


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        cache = defaultdict(lambda: [-1, -1])
        for idx, c in enumerate(s):
            idx_1st, idx_2nd = cache[c]
            dp[idx + 1] = dp[idx] + idx - (idx_2nd << 1) + idx_1st
            cache[c] = [idx_2nd, idx]

        return sum(dp)


assert_value(10, Solution().uniqueLetterString, s="ABC")
assert_value(8, Solution().uniqueLetterString, s="ABA")
assert_value(92, Solution().uniqueLetterString, s="LEETCODE")
