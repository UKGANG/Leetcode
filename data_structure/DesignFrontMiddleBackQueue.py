'''
1670. Design Front Middle Back Queue
https://leetcode.com/problems/design-front-middle-back-queue/
'''
from typing import List

from test_tool import assert_value


class FrontMiddleBackQueue:
    def __init__(self):
        self.front_queue = []
        self.reversed_queue = []

    def pushFront(self, val: int) -> None:
        self.front_queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.rebalance()
        self.front_queue.append(val)

    def pushBack(self, val: int) -> None:
        self.reversed_queue.append(val)

    def popFront(self) -> int:
        if self.is_empty():
            return -1
        if self.front_queue:
            return self.front_queue.pop(0)
        return self.reversed_queue.pop()

    def popMiddle(self) -> int:
        if self.is_empty():
            return -1
        self.rebalance()
        if len(self.reversed_queue) > len(self.front_queue):
            return self.reversed_queue.pop(0)
        else:
            return self.front_queue.pop()

    def popBack(self) -> int:
        if self.is_empty():
            return -1
        if self.reversed_queue:
            return self.reversed_queue.pop()
        return self.front_queue.pop()

    def rebalance(self):
        while len(self.front_queue) > len(self.reversed_queue):
            self.reversed_queue.insert(0, self.front_queue.pop())

        while len(self.front_queue) + 1 < len(self.reversed_queue):
            self.front_queue.append(self.reversed_queue.pop(0))

    def is_empty(self):
        return not self.front_queue and not self.reversed_queue


q = FrontMiddleBackQueue()
q.pushFront(1)
q.pushBack(2)
q.pushMiddle(3)
q.pushMiddle(4)
print(q.popFront())
print(q.popMiddle())
print(q.popMiddle())
print(q.popBack())
print(q.popFront())
print()

# assert_value(3, Solution().minNumberOperations, target=[1, 2, 3, 2, 1])
