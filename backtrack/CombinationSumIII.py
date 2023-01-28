'''
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/
'''
import collections
from typing import List, Optional, NoReturn

from test_tool import assert_value


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(i):
            nonlocal curr_sum
            if curr_sum == n and len(curr) == k:
                res.append(curr[:])
                return
            for j in range(i + 1, 10):
                if curr_sum + j > n:
                    break
                if 10 - j + len(curr) < k:
                    break
                curr_sum += j
                curr.append(j)
                backtrack(j)
                curr.pop()
                curr_sum -= j

        res = []
        curr = []
        curr_sum = 0
        backtrack(0)

        return res
    def _combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(l, r, k, n):
            nonlocal res, combo
            if not n and not k:
                res.append(combo[:])
                return
            for i in range(l, r + 1):
                if n < i or r + 1 - i < k:
                    break
                combo.append(i)
                backtrack(i + 1, r, k - 1, n - i)
                combo.pop()

        res, combo = [], []
        backtrack(1, 9, k, n)
        return res


assert_value([[1, 2, 4]], Solution().combinationSum3, k=3, n=7)
assert_value([[1, 2, 6], [1, 3, 5], [2, 3, 4]], Solution().combinationSum3, k=3, n=9)
