'''
216. Combination Sum III
https://leetcode.com/problems/combination-sum-iii/
'''
import collections
from typing import List, Optional, NoReturn

from test_tool import assert_value


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
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
