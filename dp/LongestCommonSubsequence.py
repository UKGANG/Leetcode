'''
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
'''
from typing import List

from test_tool import assert_value


class Solution(object):
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)

        dp = [
            [0] * (n + 1)
            for _ in range(m + 1)
        ]

        text1 = f' {text1}'
        text2 = f' {text2}'
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]

    def _longestCommonSubsequence(self, text1: str, text2: str) -> str:
        if len(text1) == 0 or len(text2) == 0:
            return ''
        c = []
        for i in range(len(text1) + 1):
            c_inner = [0] * (len(text2) + 1)
            c.append(c_inner)

        for m in range(1, len(text1) + 1):
            for n in range(1, len(text2) + 1):
                if text1[m - 1] == text2[n - 1]:
                    c[m][n] = c[m - 1][n - 1] + 1
                else:
                    c[m][n] = max(c[m - 1][n], c[m][n - 1])

        return c[m][n]


assert_value(4, Solution().longestCommonSubsequence, text1="ABCBDAB", text2="BDCABA")
assert_value(3, Solution().longestCommonSubsequence, text1="abcde", text2="ace")
