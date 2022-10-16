'''
2101. Detonate the Maximum Bombs
https://leetcode.com/problems/detonate-the-maximum-bombs/
'''
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def dfs(source):
            res = 1
            detonated[source] = True
            for dest in range(len(bombs)):
                if detonated[dest]:
                    continue
                if pow(bombs[dest][0] - bombs[source][0], 2) + pow(bombs[dest][1] - bombs[source][1], 2) > pow(
                        bombs[source][2], 2):
                    continue
                res += dfs(dest)
            return res

        res = 0
        bombs.sort(key=lambda item: -item[2])
        detonated = [False] * len(bombs)
        for i in range(len(bombs)):

            if detonated[i]:
                continue
            detonated = [False] * len(bombs)
            res = max(res, dfs(i))
        return res
