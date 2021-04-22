'''
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
'''
from typing import List

from test_tool import assert_value


class Solution(object):
    def longestCommonSubsequence(self, text1: str, text2: str) -> str:
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
