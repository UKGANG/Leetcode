'''
716. Max Stack
https://leetcode.com/problems/max-stack/
'''
import bisect
import uuid
from collections import OrderedDict


class MaxStack:
    def __init__(self):
        self._stack = OrderedDict()
        self._sorted_list = []
        self._sorted_list_id = []

    def push(self, x: int) -> None:
        key = str(uuid.uuid4())
        self._stack[key] = x
        idx = bisect.bisect_right(self._sorted_list, x)

        self._sorted_list.insert(idx, x)
        self._sorted_list_id.insert(idx, key)

    def pop(self) -> int:
        key, x = self._stack.popitem(last=True)
        idx = bisect.bisect_right(self._sorted_list, x)
        if idx == len(self._sorted_list) or x != self._sorted_list[idx]:
            idx -= 1
        del self._sorted_list[idx]
        del self._sorted_list_id[idx]
        return x

    def top(self) -> int:
        return next(reversed(self._stack.items()))[1]

    def peekMax(self) -> int:
        return self._sorted_list[-1]

    def popMax(self) -> int:
        x = self._sorted_list.pop()
        key = self._sorted_list_id.pop()
        del self._stack[key]
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
