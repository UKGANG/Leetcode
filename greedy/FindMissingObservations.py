"""
2028. Find Missing Observations
https://leetcode.com/problems/find-missing-observations/description/
"""
from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        missing_val, residual = divmod((mean * (m + n) - sum(rolls)), n)
        if not 0 < missing_val < 7:
            return []
        if missing_val == 6 and residual:
            return []
        missing_arr = [missing_val] * n
        for i in range(residual):
            missing_arr[i] += 1

        return missing_arr
