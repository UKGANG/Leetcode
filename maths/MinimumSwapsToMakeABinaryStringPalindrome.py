'''
Minimum Swaps To Make A Binary String Palindrome
https://leetcode.com/discuss/interview-question/1982251/amazon-oa-usa-sde2-minimum-swaps-to-make-a-binary-string-palindrome
'''
from typing import List

from test_tool import assert_value


class Solution:
    def minSwap(self, s: str) -> int:
        cnt = 0
        for i in range(len(s) >> 1):
            cnt += 1
        if cnt & 1 == 0:
            return cnt >> 1
        if len(s) & 1:
            return (cnt + 1) >> 1
        return -1


assert_value(2, Solution().minSwap, s='0100101')
