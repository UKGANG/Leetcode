'''
641. Design Circular Deque
https://leetcode.com/problems/design-circular-deque/
'''
from test_tool import assert_value


class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.limit = k
        self.size = 0
        self.front_queue = []
        self.back_queue = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.size += 1
        self.front_queue.insert(0, value)
        self.rebalance()
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.size += 1
        self.back_queue.append(value)
        self.rebalance()
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.front_queue:
            self.front_queue.pop(0)
        else:
            self.back_queue.pop(0)
        self.size -= 1
        self.rebalance()
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        if self.back_queue:
            self.back_queue.pop()
        else:
            self.front_queue.pop()
        self.size -= 1
        self.rebalance()
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if self.isEmpty():
            return -1
        if self.front_queue:
            return self.front_queue[0]
        else:
            return self.back_queue[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if self.isEmpty():
            return -1
        if self.back_queue:
            return self.back_queue[-1]
        else:
            return self.front_queue[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return not bool(self.size)

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self.size == self.limit

    def rebalance(self):
        """
        Rebalances the first and the second half of the storage
        :return:
        """
        while len(self.front_queue) > len(self.back_queue):
            self.back_queue.insert(0, self.front_queue.pop())

        while len(self.front_queue) + 1 < len(self.back_queue):
            self.front_queue.append(self.back_queue.pop(0))


circularDeque = MyCircularDeque(3)
assert_value(True, circularDeque.insertLast, value=1)
assert_value(True, circularDeque.insertLast, value=2)
assert_value(True, circularDeque.insertFront, value=3)
assert_value(False, circularDeque.insertFront, value=4)
assert_value(2, circularDeque.getRear)
assert_value(True, circularDeque.isFull)
assert_value(True, circularDeque.deleteLast)
assert_value(True, circularDeque.insertFront, value=4)
assert_value(4, circularDeque.getFront)

circularDeque = MyCircularDeque(8)
assert_value(True, circularDeque.insertFront, value=5)
assert_value(5, circularDeque.getFront)
assert_value(False, circularDeque.isEmpty)
assert_value(True, circularDeque.deleteFront)
assert_value(True, circularDeque.insertLast, value=3)
assert_value(3, circularDeque.getRear)
assert_value(True, circularDeque.insertLast, value=7)
assert_value(True, circularDeque.insertFront, value=7)
assert_value(True, circularDeque.deleteLast)
assert_value(True, circularDeque.insertLast, value=4)
assert_value(False, circularDeque.isEmpty)
