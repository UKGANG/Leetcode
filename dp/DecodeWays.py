'''
91. Decode Ways
https://leetcode.com/problems/decode-ways/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        for idx in range(1, len(s)):
            if int(s[idx - 1:idx + 1]) < 10:
                if s[idx] == '0':
                    return 0
                dp[idx + 1] = dp[idx]
            elif int(s[idx - 1:idx + 1]) > 26:
                if s[idx] == '0':
                    return 0
                else:
                    dp[idx + 1] = dp[idx]
            elif s[idx] == '0':
                dp[idx + 1] = dp[idx - 1]
            else:
                dp[idx + 1] = dp[idx] + dp[idx - 1]

        return dp[-1]


assert_value(2, Solution().numDecodings, s="12")
assert_value(3, Solution().numDecodings, s="226")
assert_value(0, Solution().numDecodings, s="06")
assert_value(3, Solution().numDecodings, s="1201234")
