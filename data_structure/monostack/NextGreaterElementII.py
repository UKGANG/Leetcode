'''
503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums) * 2):
            i %= len(res)
            n = nums[i]
            while stack and stack[-1][-1] < n:
                i_prev, n_prev = stack.pop()
                if i_prev != i:
                    res[i_prev] = n
            stack.append((i, n))
        return res


assert_value([2, -1, 2], Solution().nextGreaterElements, nums=[1, 2, 1])
assert_value([2, 3, 4, -1, 4], Solution().nextGreaterElements, nums=[1, 2, 3, 4, 3])
