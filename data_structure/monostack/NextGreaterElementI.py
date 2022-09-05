'''
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cache = [-1] * len(nums2)

        stack = []
        for curr in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[curr]:
                prev = stack.pop()
                cache[prev] = nums2[curr]
            stack.append(curr)

        reversed_idx = {n: idx for idx, n in enumerate(nums2)}
        return [cache[reversed_idx[num]] for num in nums1]

    def _nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_nums2 = {n: i for i, n in enumerate(nums2)}
        stack = []
        max_right = [-1] * len(nums2)
        for i, n in enumerate(nums2):
            while stack and stack[-1][-1] < n:
                i_prev, n_prev = stack.pop()
                max_right[i_prev] = n
            stack.append((i, n))
        return [max_right[idx_nums2[n]] for n in nums1]


assert_value([-1, 3, -1], Solution().nextGreaterElement, nums1=[4, 1, 2], nums2=[1, 3, 4, 2])
assert_value([3, -1], Solution().nextGreaterElement, nums1=[2, 4], nums2=[1, 2, 3, 4])
