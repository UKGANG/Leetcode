"""
Maximum Index
https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/?ref=gcse
"""
from typing import List
from test_tool import assert_value


class Solution:
    def maximumIndex(self, arr: List[int]) -> int:
        n = len(arr)
        index = {}
        for i in range(n):
            if arr[i] in index:
                index[arr[i]].append(i)
            else:
                index[arr[i]] = [i]
        arr.sort()
        res = 0

        left = n
        for i in range(n):
            if left > index[arr[i]][0]:
                left = index[arr[i]][0]
            right = index[arr[i]][-1]
            res = max(res, right - left)
        return res

    def _cache_maximumIndex(self, arr: List[int]) -> int:
        n = len(arr)
        res = -1
        max_left = [-float('inf')] * n
        max_left[-1] = arr[-1]
        for i in range(n - 2, -1, -1):
            max_left[i] = max(max_left[i + 1], arr[i])

        for i in range(n):
            l, r = i + 1, n - 1
            while l <= r:
                m = l + ((r - l) >> 1)
                if arr[i] <= max_left[m]:
                    res = max(res, m - i)
                    l = m + 1
                else:
                    r = m - 1

        return res

    def _maximumIndex_brute_force(self, arr: List[int]) -> int:
        n = len(arr)
        res = -1
        for x in range(n - 1):
            for y in range(n - 1, x, -1):
                if arr[x] > arr[y]:
                    continue
                res = max(res, y - x)
                break
        return res


# assert_value(1, Solution().maximumIndex, arr=[1, 10])
assert_value(6, Solution().maximumIndex, arr=[34, 8, 10, 3, 2, 80, 30, 33, 1])
# assert_value(8, Solution().maximumIndex, arr=[9, 2, 3, 4, 5, 6, 7, 8, 18, 0])
# assert_value(5, Solution().maximumIndex, arr=[1, 2, 3, 4, 5, 6])
# assert_value(-1, Solution().maximumIndex, arr=[6, 5, 4, 3, 2, 1])
