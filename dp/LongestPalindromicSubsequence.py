'''
Longest Palindromic Subsequence | DP-12
https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
'''
from typing import List

from test_tool import assert_value

class Solution:
    def longestPalindromicSubsequence(self, s: str) -> str:
        dp = []
        for i in range(len(s)):
            dp.append([0] * len(s))
            dp[i][i] = 1

        for width in range(2, len(s) + 1):
            for start in range(len(s) - width + 1):
                end = start + width - 1
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                else:
                    dp[start][end] = max(dp[start][end - 1], dp[start + 1][end])

        return dp[0][len(s) - 1]


# BABCBAB
assert_value(7, Solution().longestPalindromicSubsequence, s='BBABCBCAB')
# EEKEE
assert_value(5, Solution().longestPalindromicSubsequence, s='GEEKSFORGEEKS')