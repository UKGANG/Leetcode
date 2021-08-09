'''
341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/
'''
from typing import List

from test_tool import assert_value


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def generator(nestedList: [NestedInteger]):
            for e in nestedList:
                if e.isInteger():
                    yield e.getInteger()
                else:
                    for _e in generator(e.getList()):
                        yield _e

        self._generator = generator(nestedList)
        self._val = None

    def next(self) -> int:
        return self._val

    def hasNext(self) -> bool:
        try:
            self._val = next(self._generator)
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
