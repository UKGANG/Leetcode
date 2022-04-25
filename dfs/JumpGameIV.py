'''
1345. Jump Game IV
https://leetcode.com/problems/jump-game-iv/
'''
import collections
from typing import List

from test_tool import assert_value


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        route = collections.defaultdict(list)
        for i in range(len(arr)):
            route[arr[i]].append(i)
        visited = set()
        q = [0]
        res = 0
        while q:
            q_next = []
            for idx in q:
                if idx == len(arr) - 1:
                    return res
                visited.add(idx)
                if 0 <= idx - 1 and idx - 1 not in visited:
                    q_next.append(idx - 1)
                if idx + 1 < len(arr) and idx + 1 not in visited:
                    q_next.append(idx + 1)
                q_next.extend(route[arr[idx]][::-1])
                del route[arr[idx]]
            res += 1
            q = q_next
        return res


assert_value(3, Solution().minJumps, arr=[100, -23, -23, 404, 100, 23, 23, 23, 3, 404])
assert_value(0, Solution().minJumps, arr=[7])
assert_value(1, Solution().minJumps, arr=[7, 6, 9, 6, 9, 6, 9, 7])
assert_value(3, Solution().minJumps, arr=[11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13])
