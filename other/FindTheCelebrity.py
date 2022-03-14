'''
645 · Find the Celebrity
https://www.lintcode.com/problem/645/description
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def findCelebrity(self, n):
        candidate = 0
        for i in range(n):
            if Celebrity.knows(candidate, i):
                candidate = i

        for i in range(n):
            if candidate == i:
                continue
            if Celebrity.knows(candidate, i) or not Celebrity.knows(i, candidate):
                return -1
        return candidate


    def findCelebrity(self, n):
        celeb = 0

        for i in range(1, n):
            if Celebrity.knows(celeb, i):
                celeb = i

        # Check if the final candicate is the celebrity
        for i in range(n):
            if celeb != i and Celebrity.knows(celeb, i):
                return -1
            if celeb != i and not Celebrity.knows(i, celeb):
                return -1

        return celeb


    def execute(self, graph: List[List[int]]) -> int:
        Celebrity.graph = graph
        return self.findCelebrity(len(graph))


class Celebrity:
    graph = None

    @staticmethod
    def knows(i, j):
        return Celebrity.graph[i][j] == 1


assert_value(1, Solution().execute, graph=[
    [1, 1, 0],
    [0, 1, 0],
    [1, 1, 1]
])
assert_value(-1, Solution().execute, graph=[
    [1, 0, 1],
    [1, 1, 0],
    [0, 1, 1]
])

assert_value(0, Solution().execute, graph=[
    [1, 0, 0],
    [1, 1, 0],
    [1, 1, 1]
])
