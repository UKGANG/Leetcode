'''
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/
'''
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        size = len(isConnected)
        visited = []
        for i in range(size):
            visited.append([False] * size)

        res = 0
        for i in range(size):
            for j in range(size):
                if visited[i][j]:
                    continue
                visited[i][j] = True
                if not isConnected[i][j]:
                    continue
                res += 1
                pending_visit = [(i, j)]
                # Visit this province
                self.explore(pending_visit, isConnected, visited)

        return res

    def explore(self, pending_visit: List[Tuple[int, int]], isConnected: List[List[int]],
                visited: List[List[int]]) -> None:
        size = len(visited)
        while pending_visit:
            i, j = pending_visit.pop()
            for idx in range(size):
                if visited[i][idx]:
                    continue
                if not isConnected[i][idx]:
                    continue
                visited[i][idx] = True
                pending_visit.append((i, idx))
            for idx in range(size):
                if visited[idx][j]:
                    continue
                if not isConnected[idx][j]:
                    continue
                visited[idx][j] = True
                pending_visit.append((idx, j))


assert_value(2, Solution().findCircleNum, isConnected=[
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
])
assert_value(3, Solution().findCircleNum, isConnected=[
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])
assert_value(1, Solution().findCircleNum, isConnected=[
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1]
])
