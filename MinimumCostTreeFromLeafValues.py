'''
1130. Minimum Cost Tree From Leaf Values
https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        arr = arr.copy()
        res = 0
        while len(arr) > 1:
            min_val = min(arr)
            min_idx = arr.index(min_val)
            left_val = float("inf")
            right_val = float("inf")
            if 0 < min_idx:
                left_val = arr[min_idx - 1]
            if min_idx < len(arr) - 1:
                right_val = arr[min_idx + 1]
            res += min(left_val, right_val) * min_val
            arr.pop(min_idx)
        return res

    def _mctFromLeafValues(self, arr: List[int]) -> int:
        cache = {}
        return self._dp(0, len(arr), arr, cache)

    def _dp(self, i, j, arr, cache):
        if 1 == j - i:  # len == 1
            return 0
        if (i, j) in cache:
            return cache[(i, j)]

        res = float("inf")
        for k in range(i + 1, j):
            left = self._dp(i, k, arr, cache)
            right = self._dp(k, j, arr, cache)
            root = max(arr[i:k]) * max(arr[k:j])
            total = left + root + right
            res = min(total, res)
        cache[(i, j)] = res
        return res


assert_value(32, Solution().mctFromLeafValues, arr=[6, 2, 4])
