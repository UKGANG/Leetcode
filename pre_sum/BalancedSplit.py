'''
Balanced Split
https://leetcode.com/discuss/interview-question/718692/facebook-training-balanced-split
'''
from test_tool import assert_value


def balancedSplitExists(arr):
    if len(arr) < 2:
        return False
    A = sorted(arr)
    sum_A = sum(A)
    sum_B = 0
    i = len(arr) - 1
    while True:
        curr = A[i]
        i -= 1
        sum_A -= curr
        sum_B += curr
        if sum_A == sum_B:
            if A[i] < curr:
                return True
            else:
                return False

    return False


assert_value(True, balancedSplitExists, arr=[1, 5, 7, 1])
assert_value(False, balancedSplitExists, arr=[12, 7, 6, 7, 6])
