'''
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._opt = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in self._opt:
                b = stack.pop()
                a = stack.pop()
                res = self._opt[token](a, b)
                stack.append(res)
            else:
                stack.append(int(token))
        return stack[0]


assert_value(9, Solution().evalRPN, tokens=["2", "1", "+", "3", "*"])
assert_value(6, Solution().evalRPN, tokens=["4", "13", "5", "/", "+"])
assert_value(22, Solution().evalRPN, tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
