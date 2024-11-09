"""
415. Add Strings
https://leetcode.com/problems/add-strings/
"""
import itertools
import re
from collections import deque
from typing import List

from test_tool import assert_value
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        int_map = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }
        idx_1 = idx_2 = 0
        carry = 0
        res = deque([])
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        for idx in range(max(len(num1), len(num2))):
            n1 = 0 if idx >= len(num1) else int_map[num1[idx]]
            n2 = int_map[num2[idx]]
            n = n1 + n2 + carry
            res.appendleft(n % 10)
            carry = n // 10
        if carry:
            res.appendleft(carry)
        return ''.join(map(str, res))