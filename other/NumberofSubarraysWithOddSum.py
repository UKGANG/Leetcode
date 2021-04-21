'''
1524. Number of Sub-arrays With Odd Sum
https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def numOfSubarrays(self, A: List[int]) -> int:
        mod = 10 ** 9 + 7
        n = len(A)
        preSum = [0, A[0]]
        for i in range(1, n):
            preSum.append(preSum[-1] + A[i])

        even = 0
        odd = 0

        for i in preSum:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1

        return (odd * even) % mod


assert_value(4, Solution().numOfSubarrays, A=[1, 3, 5])
assert_value(0, Solution().numOfSubarrays, A=[2, 4, 6])
assert_value(16, Solution().numOfSubarrays, A=[1, 2, 3, 4, 5, 6, 7])
assert_value(4, Solution().numOfSubarrays, A=[100, 100, 99, 99])
assert_value(3, Solution().numOfSubarrays, A=[100, 99, 99])
assert_value(1, Solution().numOfSubarrays, A=[7])
