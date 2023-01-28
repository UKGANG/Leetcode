'''
40. Combination Sum II
https://leetcode.com/problems/combination-sum-ii/
'''
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, residual):
            if combo and not residual:
                res.append(combo[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                num = candidates[i]
                if residual < num:
                    break
                combo.append(num)
                backtrack(i + 1, residual - num)
                combo.pop()

        res, combo = [], []
        candidates.sort()
        backtrack(0, target)
        return res
