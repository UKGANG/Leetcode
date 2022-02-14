'''
284. Peeking Iterator
https://leetcode.com/problems/peeking-iterator/
'''
from typing import List

from test_tool import assert_value


# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._peeked_data = None
        self._is_peeked = False
        self._iterator = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # Try preparing for the peek operation
        if not self._is_peeked and self._iterator.hasNext():
            self._peeked_data = self._iterator.next()
            self._is_peeked = True

        # Return None if preparation did nothing
        if not self._is_peeked:
            return None

        return self._peeked_data

    def next(self):
        """
        :rtype: int
        """
        if self._is_peeked:
            res = self._peeked_data
            self._peeked_data = None
            self._is_peeked = False
            return res
        if self._iterator.hasNext():
            return self._iterator.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._is_peeked or self._iterator.hasNext()

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
