'''
716. Max Stack
https://leetcode.com/problems/max-stack/
'''
from typing import List

from test_tool import assert_value


class MaxStack:
    def __init__(self):
        self._stack = []
        self._max_stack = []

    def push(self, x: int):
        self._stack.append(x)
        if not self._max_stack or self._max_stack[-1] <= x:
            self._max_stack.append(x)

    def pop(self):
        x = self._stack.pop()
        if x == self._max_stack[-1]:
            self._max_stack.pop()
        return x

    def top(self):
        return self._stack[-1]

    def peekMax(self):
        return self._max_stack[-1]

    def popMax(self):
        x = self._max_stack.pop()
        tmp_stack = []
        while True:
            y = self._stack.pop()
            if x == y:
                break
            tmp_stack.append(y)

        while tmp_stack:
            self.push(tmp_stack.pop())

        return x


stack = MaxStack()
stack.push(5)
stack.push(1)
stack.push(5)
assert 5 == stack.top()
assert 5 == stack.popMax()
assert 1 == stack.top()
assert 5 == stack.peekMax()
assert 1 == stack.pop()
assert 5 == stack.top()
