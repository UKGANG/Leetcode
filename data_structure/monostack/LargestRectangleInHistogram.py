'''
84. Largest Rectangle in Histogram
https://leetcode.com/problems/largest-rectangle-in-histogram/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Exclusive
        dp_idx_left = [-1] * n
        for i in range(1, n):
            l = i - 1
            while l >= 0 and heights[l] >= heights[i]:
                l = dp_idx_left[l]
            dp_idx_left[i] = l

        dp_idx_right = [n] * n
        for i in range(n - 2, -1, -1):
            r = i + 1
            while r <= n - 1 and heights[r] >= heights[i]:
                r = dp_idx_right[r]
            dp_idx_right[i] = r

        res = 0
        for i in range(n):
            w = dp_idx_right[i] - dp_idx_left[i] - 1
            h = heights[i]
            res = max(res, w * h)

        return res

    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0

        stack = []

        heights.insert(0, 0)
        heights.append(0)

        for curr in range(len(heights)):
            while stack and heights[stack[-1]] > heights[curr]:
                mid = stack.pop()

                w = curr - stack[-1] - 1
                h = heights[mid]
                res = max(res, w * h)
            stack.append(curr)
        return res

    def _largestRectangleArea(self, heights: List[int]) -> int:
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
assert_value(3, Solution().largestRectangleArea, heights=[2, 1, 2])
