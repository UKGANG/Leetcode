'''
2 Stack Queue
'''
from typing import List

from test_tool import assert_value


class TwoStackQueue:
    def __init__(self):
        self._stack_input = []
        self._stack_output = []

    def size(self):
        return len(self._stack_input) + len(self._stack_output)

    def push(self, val: int):
        self._stack_input.append(val)

    def pop(self):
        if not self._stack_output:
            self._stack_input, self._stack_output = self._stack_output, self._stack_input
        if not self._stack_output:
            return None
        return self._stack_output.pop()


nums = list(range(100))

heap = TwoStackQueue()
for num in nums:
    heap.push(num)

for i in reversed(range(len(nums))):
    assert_value(i, heap.pop)
