'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/
'''
from typing import List, Tuple

from test_tool import assert_value


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target):
            if not target and combo:
                res.append(combo[:])
                return
            for i in range(start, len(candidates)):
                if target < candidates[i]:
                    break
                combo.append(candidates[i])
                backtrack(i, target - candidates[i])
                combo.pop()

        candidates.sort()
        res, combo = [], []
        backtrack(0, target)
        return res

    def _combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtrack(candidates, target, [], res)
        return res

    def backtrack(self, candidates: Tuple[int], target: int, path: List[int], res: List[int]) -> None:
        if target == 0:
            res.append(path)
        for num in candidates:
            if num > target:
                break
            if not path or num >= path[-1]:
                self.backtrack(candidates, target - num, path + [num], res)


assert_value([[2, 2, 3], [7]], Solution().combinationSum, candidates=[2, 3, 6, 7], target=7)
assert_value([[2, 2, 2, 2], [2, 3, 3], [3, 5]], Solution().combinationSum, candidates=[2, 3, 5], target=8)
