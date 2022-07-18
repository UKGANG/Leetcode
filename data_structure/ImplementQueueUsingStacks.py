'''
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
'''


class MyQueue:

    def __init__(self):
        self._tail_stack = []
        self._head_stack = []

    def push(self, x: int) -> None:
        self._tail_stack.append(x)

    def pop(self) -> int:
        res = self.peek()
        if res:
            self._head_stack.pop()
        return res

    def peek(self) -> int:
        if not self._head_stack:
            while self._tail_stack:
                self._head_stack.append(self._tail_stack.pop())
        if not self._head_stack:
            return None
        return self._head_stack[-1]

    def empty(self) -> bool:
        return self.peek() is None

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()