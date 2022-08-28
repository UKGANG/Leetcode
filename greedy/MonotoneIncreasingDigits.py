'''
738. Monotone Increasing Digits
https://leetcode.com/problems/monotone-increasing-digits/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        nine = None
        for i in range(len(digits) - 2, -1, -1):
            if digits[i] > digits[i + 1]:
                nine = i + 1
                digits[i] -= 1
        if nine is not None:
            digits[nine:] = [9] * (len(digits) - nine)
        return int(''.join([str(i) for i in digits]))
