'''
516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/
https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [
            [0] * n
            for _ in range(n)
        ]

        for i in range(n):
            dp[i][i] = 1

        for width in range(2, n + 1):
            for start in range(n - width + 1):
                end = start + width - 1
                if s[start] == s[end]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                else:
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

        return dp[0][-1]

    def _timeout_longestPalindromeSubseq(self, s: str) -> int:
        def search(l, r):
            if l == r:
                return 1
            if l + 1 == r:
                if s[l] == s[r]:
                    return 2
                return 0
            if s[l] == s[r]:
                return search(l + 1, r - 1) + 2
            return max(search(l + 1, r), search(l, r - 1))

        return search(0, len(s) - 1)

    def _prev_edition_longestPalindromicSubsequence(self, s: str) -> str:
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
