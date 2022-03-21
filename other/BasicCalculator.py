'''
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        op = '+'
        num = ''
        for c in s:
            if not c.strip():
                continue
            if ')' == c:
                if op == '+':
                    curr += int(num) if num else 0
                else:
                    curr -= int(num) if num else 0
                num = curr
                op, curr = stack.pop()
                if op == '+':
                    curr += num
                else:
                    curr -= num
                num = ''

            if '(' == c:
                stack.append((op, curr))
                op = '+'
                curr = 0
            else:
                if c.isnumeric():
                    num += c
                else:
                    if op == '+':
                        curr += int(num) if num else 0
                    else:
                        curr -= int(num) if num else 0
                    op = c
                    num = ''

        if op == '+':
            curr += int(num) if num else 0
        else:
            curr -= int(num) if num else 0
        return curr


assert_value(2, Solution().calculate, s="1 + 1")
assert_value(3, Solution().calculate, s=" 2-1 + 2 ")
assert_value(23, Solution().calculate, s="(1+(4+5+2)-3)+(6+8)")
