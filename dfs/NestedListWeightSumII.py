'''
364. Nested List Weight Sum II
https://leetcode.com/problems/nested-list-weight-sum-ii/
'''

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
from typing import List, NoReturn


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def dfs(nested_int: NestedInteger, depth: int) -> NoReturn:
            nonlocal max_depth, curr_sum, curr_weighted_sum
            if nested_int.isInteger():
                curr_sum += nested_int.getInteger()
                curr_weighted_sum += depth * nested_int.getInteger()
                return
            if nested_int.getList():
                max_depth = max(max_depth, depth + 1)
            for element in nested_int.getList():
                dfs(element, depth + 1)

        max_depth, curr_sum, curr_weighted_sum = 1, 0, 0
        for element in nestedList:
            dfs(element, 1)

        return (max_depth + 1) * curr_sum - curr_weighted_sum
