'''
Contiguous Subarrays
https://leetcode.com/discuss/interview-question/579606/count-contiguous-subarrays
'''
import bisect
from typing import List

from test_tool import assert_value


def count_subarrays(arr: List[int]) -> List[int]:
    ending = [0] * len(arr)
    starting = [0] * len(arr)

    cache_arr = [arr[0]]
    cache_idx = [0]
    for i in range(1, len(arr)):
        p = bisect.bisect(cache_arr, arr[i])
        cache_arr.insert(p, arr[i])
        cache_idx.insert(p, i)
        if arr[i - 1] > arr[i]:
            ending[i] = 0
            continue
        if p == len(cache_idx) - 1:
            ending[i] = len(cache_idx) - 1
        else:
            p_max = min(cache_idx[p + 1:])
            ending[i] = i - p_max - 1

    cache_arr = [arr[-1]]
    cache_idx = [len(arr) - 1]
    for i in reversed(range(len(arr) - 1)):
        p = bisect.bisect(cache_arr, arr[i])
        cache_arr.insert(p, arr[i])
        cache_idx.insert(p, i)
        if arr[i + 1] > arr[i]:
            starting[i] = 0
            continue
        if p == len(cache_idx) - 1:
            starting[i] = len(cache_idx) - 1
        else:
            p_min = min(cache_idx[p + 1:])
            starting[i] = p_min - i - 1

    res = []
    for e, s in zip(ending, starting):
        res.append(e + s + 1)

    return res


assert_value([1, 3, 1, 5, 1], count_subarrays, arr=[3, 4, 1, 6, 2])
assert_value([1, 2, 6, 1, 3, 1], count_subarrays, arr=[2, 4, 7, 1, 5, 3])
