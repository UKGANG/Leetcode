'''
772. Basic Calculator III
https://leetcode.com/problems/basic-calculator-iii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        stack = []
        expr = ''
        for c in s:
            if c == '(':
                stack.append(expr)
                expr = ''
            elif c == ')':
                try:
                    num = self._calculate_v2(expr)
                except:
                    print()
                expr = stack.pop() if stack else ''
                # edge cases
                if num < 0:
                    if not expr:
                        expr = str(num)
                        continue
                    if expr[-1] == '-':
                        expr = expr[: -1] + '+'
                        num *= -1
                    elif expr[-1] == '+':
                        expr = expr[: -1]
                    else:
                        if expr[0] == '-':
                            expr = expr[1:]
                        else:
                            expr = '-' + expr
                        num *= -1

                expr = f'{expr}{num}'
            else:
                expr += c

        return self._calculate_v2(expr)

    def _calculate_v2(self, s: str) -> int:
        s = s.replace(" ", "")
        num = ''
        stack = []
        idx = 0
        while idx < len(s):
            c = s[idx]
            if s[idx].isnumeric():
                num += c
                idx += 1
                continue
            if num:
                stack.append(int(num))
            if c == '+':
                num = ''
                idx += 1
            elif c == '-':
                num = '-'
                idx += 1
            else:
                curr = stack.pop()
                idx += 1
                num = ''
                while idx < len(s) and s[idx].isnumeric():
                    num += s[idx]
                    idx += 1
                if c == '*':
                    curr *= int(num)
                else:
                    curr /= int(num)
                    curr = int(curr)
                num = ''
                stack.append(curr)
        if not num:
            num = '0'
        num = int(num)
        return sum(stack) + num


assert_value(2, Solution().calculate, s="1 + 1")
assert_value(4, Solution().calculate, s="6-4/2")
assert_value(21, Solution().calculate, s="2*(5+5*2)/3+(6/2+8)")
assert_value(3, Solution().calculate, s="2-(5-6)")
assert_value(-40, Solution().calculate, s="((((8+3)*(4-10))-2)+((5+(10/2))+((9+5)+(2+2))))")
assert_value(355857, Solution().calculate,
             s="((13/((6+19)/14))+((17*(((((((18+19)+(5+7))*(17+(14/16)))+7)/((((14+14)+(7/10))*15)/(((20+4)*13)+1)))*(10+15))-((((((4+17)+(4*6))+(12+15))+5)+((((14+19)+(10+1))-((11+17)+(10+1)))+(((13+20)-(18+17))-((7/15)-(7-19)))))-((17+(((15+2)*(2-6))+((6+14)+(19*2))))/((((18-3)+(6*13))+15)+(((17-19)+(2+10))+((8+18)+(9+8))))))))-(((((14/5)+((((13+11)-(3*20))-((15*10)+(14+19)))-(((8+20)-(5*16))*((13-1)/(8/6)))))+8)+5)/(((((((18+17)+(4+8))+((19*16)+(11*14)))+(((6+19)*(7-17))+((12+16)*(15+7))))*((((3+13)+(19+19))-((4*7)+11))*18))-((14+20)*((((12*8)*(7+12))/13)*(((3-6)+(8/10))+(2+(15-20))))))+((((1*((12-1)+(7*18)))*6)+((((4+20)-2)*((8-13)*(14-19)))*(((19+1)+(4-13))+((19+4)*(19+19)))))+(((7+(9+(14+4)))-9)*((5/((19+3)+(9*15)))+(((20+12)+(17+12))*((17+6)+16)))))))))")
