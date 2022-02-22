'''
Element Swapping
https://leetcode.com/discuss/interview-question/848430/element-swapping-facebook-coding-practice-2020
'''
from typing import List

from test_tool import assert_value


def findMinArray(arr, k):
    if not k:
        return arr
    min_val = arr[0]
    min_idx = 0
    for idx, val in enumerate(arr[:k + 1]):
        if min_val > val:
            min_idx = idx
            min_val = val
    return [min_val] + findMinArray(arr[:min_idx] + arr[min_idx + 1:], k - min_idx)


assert_value([1, 5, 3], findMinArray, arr=[5, 3, 1], k=2)
assert_value([2, 8, 9, 11, 1], findMinArray, arr=[8, 9, 11, 2, 1], k=3)
