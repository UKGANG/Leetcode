"""
44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/
"""
import bisect
import collections
from typing import List, NoReturn

from test_tool import assert_value


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_cleaned = []
        has_star = False
        for token in p:
            if token == '*':
                if has_star:
                    continue
                has_star = True
                p_cleaned.append(token)
            else:
                has_star = False
                p_cleaned.append(token)
        p = ''.join(p_cleaned)
        if p == '*':
            return True

        m, n = len(p) + 1, len(s) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True

        s = ' ' + s
        p = ' ' + p
        for i in range(1, m):
            if p[i] == '?':
                for j in range(1, n):
                    dp[i][j] = dp[i - 1][j - 1]
            elif p[i] == '*':
                j = 0
                while j < n and not dp[i - 1][j]:
                    j += 1
                if j == n:
                    continue
                dp[i][j:] = [True] * (n - j)
            else:
                for j in range(1, n):
                    dp[i][j] = dp[i - 1][j - 1] and p[i] == s[j]
        return dp[-1][-1]

    def isMatchRecursion(self, s: str, p: str) -> bool:
        def isValid(source: str, pattern: str) -> NoReturn:
            if (source, pattern) in seen:
                return
            elif source == pattern:
                seen[(source, pattern)] = True
            elif pattern == '*':
                seen[(source, pattern)] = True
            elif not pattern or not source:
                seen[(source, pattern)] = False
            elif source[0] == pattern[0] or pattern[0] == "?":
                isValid(source[1:], pattern[1:])
                seen[(source, pattern)] = seen[(source[1:], pattern[1:])]
            elif pattern[0] == '*':
                isValid(source, pattern[1:])
                seen[(source, pattern)] = seen[(source, pattern[1:])]
                if seen[(source, pattern)]:
                    return
                isValid(source[1:], pattern)
                seen[(source, pattern)] = seen[(source[1:], pattern)]
            else:
                seen[(source, pattern)] = source[0] == pattern[0]

        p_cleaned = []
        has_star = False
        for token in p:
            if token == '*':
                if has_star:
                    continue
                has_star = True
                p_cleaned.append(token)
            else:
                has_star = False
                p_cleaned.append(token)
        p = ''.join(p_cleaned)

        seen = {}
        isValid(s, p)
        return seen[(s, p)]


assert_value(True, Solution().isMatch, s="", p="******")
assert_value(True, Solution().isMatch, s="aasfasgaa", p="*a")
assert_value(False, Solution().isMatch, s="cb", p="?a")
assert_value(True, Solution().isMatch, s="adceb", p="*a*b")
