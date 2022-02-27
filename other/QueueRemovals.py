'''
Queue Removals
https://leetcode.com/discuss/interview-question/1039925/Facebook-Practice-question-or-Queue-Removals
'''
from typing import List

from test_tool import assert_value


def findPositions(arr, x):
    n = x
    res = []
    curr = [(i, idx) for idx, i in enumerate(arr)]
    while n and curr:
        arr_sub = curr[:x]
        arr_sub_new = []

        curr_max_val, curr_max_idx = arr_sub[0][0], 0
        for idx_sub, (i, idx) in enumerate(arr_sub):
            if i > curr_max_val:
                curr_max_val = i
                curr_max_idx = idx_sub
            arr_sub_new.append((max(i - 1, 0), idx))
        res.append(arr_sub_new[curr_max_idx][1] + 1)
        del arr_sub_new[curr_max_idx]

        curr = curr[x:]
        curr.extend(arr_sub_new)
        n -= 1

    return res


assert_value([5, 6, 4, 1, 2], findPositions, arr=[1, 2, 2, 3, 4, 5], x=5)
