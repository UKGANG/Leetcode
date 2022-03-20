'''
39. Combination Sum
https://leetcode.com/problems/combination-sum/
'''
from typing import List, Tuple

from test_tool import assert_value


class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self._combinationSum(candidates, target, [], res)
        return res

    def _combinationSum(self, candidates: Tuple[int], target: int, path: List[int], res: List[int]) -> None:
        if target == 0:
            res.append(path)
        for num in candidates:
            if num > target:
                break
            if not path or num >= path[-1]:
                self._combinationSum(candidates, target - num, path + [num], res)


assert_value([[2, 2, 3], [7]], Solution().combinationSum, candidates=[2, 3, 6, 7], target=7)
assert_value([[2, 2, 2, 2], [2, 3, 3], [3, 5]], Solution().combinationSum, candidates=[2, 3, 5], target=8)
