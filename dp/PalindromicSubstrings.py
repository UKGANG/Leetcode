'''
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.count_palindrome(s, i, i)
            res += self.count_palindrome(s, i, i + 1)
        return res

    def count_palindrome(self, s, x, y) -> int:
        res = 0
        while x >= 0 and y < len(s) and s[x] == s[y]:
            res += 1
            x -= 1
            y += 1
        return res

    def _dp_countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [
            [False] * n for _ in range(n)
        ]

        for x in range(n - 1, -1, -1):
            for y in range(x, n):
                if s[x] != s[y]:
                    continue
                if x == y or x + 1 == y or dp[x + 1][y - 1]:
                    dp[x][y] = True
        return sum(sum(dp, []))

    def _countSubstrings(self, s: str) -> int:
        n = len(s)

        res = 0
        for i in range(n):
            res += 1
            for j in range(1, min(n - i, i + 1)):
                if s[i - j] != s[i + j]:
                    break
                res += 1

        for i in range(1, n):
            if s[i - 1] != s[i]:
                continue
            res += 1
            for j in range(1, min(n - i, i)):
                if s[i - 1 - j] != s[i + j]:
                    break
                res += 1
        return res

    def _fake_dp_countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [
            [False] * n
            for _ in range(n)
        ]

        res = 0
        for i in range(n):
            dp[i][i] = True
            res += 1
            for j in range(1, min(n - i, i + 1)):
                if s[i - j] != s[i + j]:
                    break
                dp[i - j][i + j] = dp[i - j + 1][i + j - 1]
                res += 1

        for i in range(1, n):
            if s[i - 1] != s[i]:
                continue
            dp[i - 1][i] = True
            res += 1
            for j in range(1, min(n - i, i)):
                if s[i - 1 - j] != s[i + j]:
                    break
                dp[i - 1 - j][i + j] = dp[i - j][i + j - 1]
                res += 1
        return res
