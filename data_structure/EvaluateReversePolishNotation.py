'''
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def __init__(self):
        self._op = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b,
        }

    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            if token not in self._op:
                num_stack.append(int(token))
            else:
                b = num_stack.pop()
                a = num_stack.pop()
                c = self._op[token](a, b)
                num_stack.append(int(c))
        return num_stack[-1]


assert_value(9, Solution().evalRPN, tokens=["2", "1", "+", "3", "*"])
assert_value(6, Solution().evalRPN, tokens=["4", "13", "5", "/", "+"])
assert_value(22, Solution().evalRPN, tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
