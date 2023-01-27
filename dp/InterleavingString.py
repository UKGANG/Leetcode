"""
97. Interleaving String
https://leetcode.com/problems/interleaving-string/
"""
from typing import List

from test_tool import assert_value


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        x, y, z = len(s1) + 1, len(s2) + 1, len(s3) + 1
        if x + y != z + 1:
            return False

        dp = [
            [False] * y for _ in range(x)
        ]

        for i in range(x):
            for j in range(y):
                if i == j == 0:
                    dp[0][0] = True
                else:
                    if i == 0:
                        dp[0][j] = s2[j - 1] == s3[j - 1] and (j == 0 or dp[0][j - 1])
                    elif j == 0:
                        dp[i][0] = s1[i - 1] == s3[i - 1] and (i == 0 or dp[i - 1][0])
                    else:
                        dp[i][j] = (
                            dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                        ) or (
                            dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                        )
        return dp[-1][-1]


assert_value(True, Solution().isInterleave, s1="db", s2="b", s3="cbb")
assert_value(True, Solution().isInterleave, s1="", s2="", s3="a")
assert_value(True, Solution().isInterleave, s1="aabcc", s2="dbbca", s3="aadbbcbcac")
assert_value(False, Solution().isInterleave, s1="aabd", s2="abdc", s3="aabdbadc")
assert_value(False, Solution().isInterleave, s1="a", s2="", s3="c")
