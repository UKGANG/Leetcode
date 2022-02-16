'''
Pair Sums
https://afteracademy.com/blog/check-for-pair-in-an-array-with-a-given-sum
'''
import collections
from typing import List

from test_tool import assert_value


def numberOfWays(arr, k):
    # Write your code here
    cnt_dict = collections.Counter(arr)
    p = k >> 1
    res = 0
    for num, cnt in cnt_dict.items():
        if num > p:
            continue
        pair = (cnt * cnt_dict[k - num])
        if (num << 1) == k:
            pair = (cnt * (cnt - 1)) >> 1
        res += pair

    return res


assert_value(2, numberOfWays, arr=[1, 2, 3, 4, 3], k=6)
assert_value(4, numberOfWays, arr=[1, 5, 3, 3, 3], k=6)
