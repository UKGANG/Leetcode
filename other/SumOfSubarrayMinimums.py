'''
907. Sum of Subarray Minimums
https://leetcode.com/problems/sum-of-subarray-minimums/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        left = [0] * len(arr)
        right = [0] * len(arr)
        stack = []
        for idx, n in enumerate(arr):
            cnt = 1
            while stack and stack[-1][0] >= n:
                cnt += stack[-1][1]
                stack.pop()
            stack.append((n, cnt))
            left[idx] = cnt

        stack.clear()
        for idx, n in enumerate(arr[::-1]):
            idx = len(arr) - idx - 1
            cnt = 1
            while stack and stack[-1][0] > n:
                cnt += stack[-1][1]
                stack.pop()
            stack.append((n, cnt))
            right[idx] = cnt

        res = 0

        for i in range(len(arr)):
            res += arr[i] * left[i] * right[i]
        return res % (10 ** 9 + 7)


assert_value(17, Solution().sumSubarrayMins, arr=[3, 1, 2, 4])
assert_value(444, Solution().sumSubarrayMins, arr=[11, 81, 94, 43, 3])
