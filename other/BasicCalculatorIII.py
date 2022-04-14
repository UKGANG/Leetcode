'''
772. Basic Calculator III
https://leetcode.com/problems/basic-calculator-iii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._opt_map = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }

    def calculate(self, s: str) -> int:
        curr = ''
        stack = []
        for c in s:
            if c.isnumeric() or c in self._opt_map:
                curr += c
                continue
            if c == '(':
                stack.append(curr)
                curr = ''
                continue
            if c == ')':
                curr = f'{self.calculate_without_bracket(curr)}'
                if not stack:
                    curr = str(curr)
                    continue
                prev = stack.pop()
                if not prev:
                    continue

                if curr[0] == '-':
                    sign = prev[-1]
                    if sign == '-':
                        curr = f'{prev[:-1]}+{curr[1:]}'
                    elif sign == '+':
                        curr = f'{prev[:-1]}{curr}'
                    else:
                        if prev[0] == '-':
                            curr = f'{prev[1:]}{curr[1:]}'
                        else:
                            curr = f'-{prev}{curr[1:]}'
                else:
                    curr = f'{prev}{curr}'

        return int(self.calculate_without_bracket(curr))

    def calculate_without_bracket(self, s):
        s = s.replace(" ", "")
        stack = []
        prev = ''
        idx = 0
        while idx < len(s):
            c = s[idx]
            if c.isnumeric():
                prev += c
                idx += 1
                continue
            if c in '+-':
                if prev:
                    stack.append(int(prev))
                prev = c
                idx += 1
                continue
            while idx < len(s) and s[idx] in "*/":
                opt = self._opt_map[s[idx]]
                idx += 1
                curr = ''
                while idx < len(s) and s[idx].isnumeric():
                    curr += s[idx]
                    idx += 1
                prev = opt(int(prev), int(curr))

        stack.append(int(prev))
        return sum(stack)


assert_value(2, Solution().calculate, s="1 + 1")
assert_value(4, Solution().calculate, s="6-4/2")
assert_value(21, Solution().calculate, s="2*(5+5*2)/3+(6/2+8)")
assert_value(3, Solution().calculate, s="2-(5-6)")
assert_value(-40, Solution().calculate, s="((((8+3)*(4-10))-2)+((5+(10/2))+((9+5)+(2+2))))")
assert_value(355857, Solution().calculate,
             s="((13/((6+19)/14))+((17*(((((((18+19)+(5+7))*(17+(14/16)))+7)/((((14+14)+(7/10))*15)/(((20+4)*13)+1)))*(10+15))-((((((4+17)+(4*6))+(12+15))+5)+((((14+19)+(10+1))-((11+17)+(10+1)))+(((13+20)-(18+17))-((7/15)-(7-19)))))-((17+(((15+2)*(2-6))+((6+14)+(19*2))))/((((18-3)+(6*13))+15)+(((17-19)+(2+10))+((8+18)+(9+8))))))))-(((((14/5)+((((13+11)-(3*20))-((15*10)+(14+19)))-(((8+20)-(5*16))*((13-1)/(8/6)))))+8)+5)/(((((((18+17)+(4+8))+((19*16)+(11*14)))+(((6+19)*(7-17))+((12+16)*(15+7))))*((((3+13)+(19+19))-((4*7)+11))*18))-((14+20)*((((12*8)*(7+12))/13)*(((3-6)+(8/10))+(2+(15-20))))))+((((1*((12-1)+(7*18)))*6)+((((4+20)-2)*((8-13)*(14-19)))*(((19+1)+(4-13))+((19+4)*(19+19)))))+(((7+(9+(14+4)))-9)*((5/((19+3)+(9*15)))+(((20+12)+(17+12))*((17+6)+16)))))))))")
