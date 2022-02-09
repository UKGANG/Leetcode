'''
Heap implementation
Arr[(i-1)/2] Returns the parent node.
Arr[(2*i)+1] Returns the left child node.
Arr[(2*i)+2] Returns the right child node.
'''
import math
import random
from typing import List

from test_tool import assert_value


class Heap:
    def __init__(self):
        self._heap = [math.inf]
        self._top = 1

    def _heapify(self, pos):
        if self.is_leaf(pos):
            return
        pos_child = self.left_child_pos(pos)

        if self.right_child_pos(pos) < self.size() + 1:
            pos_child = pos_child if self._heap[pos_child] > self._heap[
                self.right_child_pos(pos)] else self.right_child_pos(pos)

        if self._heap[pos] < self._heap[pos_child]:
            self._heap[pos], self._heap[pos_child] = self._heap[pos_child], self._heap[pos]
            self._heapify(pos_child)

    def parent_pos(self, pos):
        return pos >> 1

    def is_leaf(self, pos):
        return len(self._heap) >> 1 <= pos < len(self._heap)

    def left_child_pos(self, pos):
        return pos << 1

    def right_child_pos(self, pos):
        return (pos << 1) + 1

    def size(self):
        return len(self._heap) - 1

    def peek(self):
        return self._heap[self._top] if self.size() else None

    def push(self, val: int):
        self._heap.append(val)
        pos = self.size()
        while self._heap[pos] > self._heap[self.parent_pos(pos)]:
            self._heap[pos], self._heap[self.parent_pos(pos)] = self._heap[self.parent_pos(pos)], self._heap[pos]
            pos = self.parent_pos(pos)

    def pop(self):
        if not self.size():
            return None
        res = self._heap[self._top]
        if self.size() > 2:
            self._heap[self._top] = self._heap[~0]
            del self._heap[~0]
            self._heapify(self._top)
        else:
            del self._heap[self._top]

        return res

    def heapify(self):
        ...

    def get_heap(self):
        return self._heap


heap = Heap()
random_nums = list(range(100))
random.shuffle(random_nums)
for num in random_nums:
    heap.push(num)

for i in reversed(range(len(random_nums))):
    assert_value(i, heap.pop)
