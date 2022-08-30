'''
473. Matchsticks to Square
https://leetcode.com/problems/matchsticks-to-square/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def backtrack(idx):
            if idx == len(matchsticks):
                return not sum(edges)

            for e_idx in range(len(edges)):
                if not edges[e_idx]:
                    continue
                if edges[e_idx] < matchsticks[idx]:
                    continue
                edges[e_idx] -= matchsticks[idx]
                if backtrack(idx + 1):
                    return True
                edges[e_idx] += matchsticks[idx]
                if edges[e_idx] == edge:
                    break
            return False

        edge, resid = divmod(sum(matchsticks), 4)
        if resid:
            return False
        matchsticks.sort(reverse=True)
        if matchsticks[0] > edge:
            return False

        edges = [edge] * 4
        return backtrack(0)
