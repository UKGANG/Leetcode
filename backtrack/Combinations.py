'''
77. Combinations
https://leetcode.com/problems/combinations/
'''
import collections
from typing import List, Optional, NoReturn

from test_tool import assert_value


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i):
            if len(curr) == k:
                res.append(curr[:])
                return
            for j in range(i, n):
                if n - j + len(curr) < k:
                    break
                curr.append(j + 1)
                backtrack(j + 1)
                curr.pop()

        res = []
        curr = []
        backtrack(0)

        return res

    def _combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(l, r, k):
            nonlocal res, combo
            if not k:
                nonlocal res
                res.append(combo[:])
                return
            for i in range(l, r + 1):
                if r + 1 - i < k:
                    return
                combo.append(i)
                backtrack(i + 1, r, k - 1)
                combo.pop()

        res = []
        combo = []
        backtrack(1, n, k)
        return res
