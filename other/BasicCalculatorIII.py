'''
772. Basic Calculator III
https://leetcode.com/problems/basic-calculator-iii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        for opt in "+-*/()":
            s = s.replace(opt, f' {opt} ')
        s = s.rstrip().lstrip()
        opt = "+"
        stack = [["+", 0, 0]]
        for token in s.split():
            if token.isnumeric():
                self.simple_caloculate(opt, token, stack)
            else:
                if token in "+-*/":
                    opt = token
                else:
                    if token == '(':
                        stack.append([opt, 0, 0])
                        opt = '+'
                    else:
                        opt, curr, prev = stack.pop()
                        self.simple_caloculate(opt, curr, stack)
        return stack[-1][1]

    def simple_caloculate(self, opt, token, stack):
        token = int(token)
        if opt == "+":
            stack[-1][2] = token
            stack[-1][1] = stack[-1][1] + token
        elif opt == "-":
            stack[-1][2] = -token
            stack[-1][1] = stack[-1][1] - token
        elif opt == "*":
            curr, prev = stack[-1][1:]
            curr, prev = curr - prev + prev * token, prev * token
            stack[-1][2] = prev
            stack[-1][1] = curr
        elif opt == "/":
            curr, prev = stack[-1][1:]
            curr, prev = curr - prev + int(prev / token), int(prev / token)
            stack[-1][2] = prev
            stack[-1][1] = curr


assert_value(-1, Solution().calculate, s="1 + 1 * 2 * (1 - 2)")
assert_value(2, Solution().calculate, s="1 + 1")
assert_value(4, Solution().calculate, s="6-4/2")
assert_value(21, Solution().calculate, s="2*(5+5*2)/3+(6/2+8)")
assert_value(3, Solution().calculate, s="2-(5-6)")
assert_value(-40, Solution().calculate, s="((((8+3)*(4-10))-2)+((5+(10/2))+((9+5)+(2+2))))")
assert_value(355857, Solution().calculate,
             s="((13/((6+19)/14))+((17*(((((((18+19)+(5+7))*(17+(14/16)))+7)/((((14+14)+(7/10))*15)/(((20+4)*13)+1)))*(10+15))-((((((4+17)+(4*6))+(12+15))+5)+((((14+19)+(10+1))-((11+17)+(10+1)))+(((13+20)-(18+17))-((7/15)-(7-19)))))-((17+(((15+2)*(2-6))+((6+14)+(19*2))))/((((18-3)+(6*13))+15)+(((17-19)+(2+10))+((8+18)+(9+8))))))))-(((((14/5)+((((13+11)-(3*20))-((15*10)+(14+19)))-(((8+20)-(5*16))*((13-1)/(8/6)))))+8)+5)/(((((((18+17)+(4+8))+((19*16)+(11*14)))+(((6+19)*(7-17))+((12+16)*(15+7))))*((((3+13)+(19+19))-((4*7)+11))*18))-((14+20)*((((12*8)*(7+12))/13)*(((3-6)+(8/10))+(2+(15-20))))))+((((1*((12-1)+(7*18)))*6)+((((4+20)-2)*((8-13)*(14-19)))*(((19+1)+(4-13))+((19+4)*(19+19)))))+(((7+(9+(14+4)))-9)*((5/((19+3)+(9*15)))+(((20+12)+(17+12))*((17+6)+16)))))))))")
