'''
225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
'''
import collections


class MyStack:
    def __init__(self):
        self._head_queue = collections.deque()
        self._tail_queue = collections.deque()

    def push(self, x: int) -> None:
        self._tail_queue.append(x)

    def pop(self) -> int:
        res = self.top()
        if res:
            self._tail_queue.popleft()
        return res

    def top(self) -> int:
        if not self._tail_queue:
            self._tail_queue, self._head_queue = self._head_queue, self._tail_queue
        while len(self._tail_queue) > 1:
            self._head_queue.append(self._tail_queue.popleft())
        if not self._tail_queue:
            return None
        return self._tail_queue[0]

    def empty(self) -> bool:
        return self.top() is None
