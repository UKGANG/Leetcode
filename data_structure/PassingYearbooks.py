'''
Passing Yearbooks
https://leetcode.com/discuss/interview-question/614096/facebook-interview-preparation-question-passing-yearbooks
'''
from typing import List

from test_tool import assert_value


def findSignatureCounts(arr):
    cycle = []

    curr = []
    for i in range(len(arr)):
        curr_i = i
        while True:
            curr_next = arr[curr_i]
            if curr_next is None:
                break
            curr.append(curr_next - 1)
            arr[curr_i] = None
            curr_i = curr_next - 1

        if curr:
            cycle.append(curr)
            curr = []

    res = [0] * len(arr)
    for sub_list in cycle:
        size = len(sub_list)
        for i in sub_list:
            res[i] = size
    return res


assert_value([2, 2], findSignatureCounts, arr=[2, 1])
assert_value([1, 1], findSignatureCounts, arr=[1, 2])
