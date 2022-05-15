'''
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        for opt in "+-()":
            s = s.replace(opt, f' {opt} ')
        s = s.rstrip().lstrip()
        sign = 1
        curr_level = [0]
        for token in s.split():
            if token in "+-":
                sign = 1 if token == '+' else -1
            elif token == '(':
                curr_level.append(sign)
                curr_level.append(0)
                sign = 1
            elif token == ')':
                n = curr_level.pop()
                sign = curr_level.pop()
                curr_level[-1] += sign * n
                sign = 1
            else:
                curr_level[-1] += sign * int(token)
        return curr_level[-1]

    def _calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        curr = 0
        op = '+'
        num = ''
        for c in s:
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
