'''
65. Valid Number
https://leetcode.com/problems/valid-number/
'''
import re
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        reg_str = r'^[+-]?' \
                  r'((\d+\.?\d*)|(\.\d+))' \
                  r'([eE][+|-]?\d+)?$'
        self._reg = re.compile(reg_str)

    def isNumber(self, s: str) -> bool:
        return bool(self._reg.search(s))


for case in ["0", ".1", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
             "-123.456e789"]:
    print(f"{case}:{Solution().isNumber(case)}")
    assert_value(True, Solution().isNumber, s=case)

for case in ["e", ".", "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]:
    print(f"{case}:{Solution().isNumber(case)}")
    assert_value(False, Solution().isNumber, s=case)
