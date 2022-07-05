'''
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for right, h_right in enumerate(heights):
            left = right
            while stack and stack[-1][-1] > h_right:
                left, h_left = stack.pop()
                res = max(res, (right - left) * h_left)
            stack.append((left, h_right))

        for left, h_left in stack:
            res = max(res, (len(heights) - left) * h_left)

        return res


assert_value(10, Solution().largestRectangleArea, heights=[2, 1, 5, 6, 2, 3])
assert_value(4, Solution().largestRectangleArea, heights=[2, 4])
assert_value(2, Solution().largestRectangleArea, heights=[2, 0, 2])
assert_value(2, Solution().largestRectangleArea, heights=[1, 1])
assert_value(3, Solution().largestRectangleArea, heights=[2,1,2])
