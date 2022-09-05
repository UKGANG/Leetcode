'''
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
'''
from typing import List

from test_tool import assert_value


class Solution:
    def _monostack_row_trap(self, height: List[int]) -> int:
        res = 0

        stack = []
        for curr in range(len(height)):
            while stack and height[stack[-1]] < height[curr]:
                prev = stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[curr]) - height[prev]
                    w = curr - stack[-1] - 1
                    res += h * w
            stack.append(curr)
        return res

    def _monostack_trap(self, height: List[int]) -> int:
        res = [0] * len(height)

        stack = []
        for curr in range(len(height)):
            while stack and height[stack[-1]] < height[curr]:
                stack.pop()
            if stack:
                res[curr] = height[stack[0]]
            stack.append(curr)

        for curr in stack:
            res[curr] = 0
        stack.clear()
        for curr in range(len(height) - 1, -1, -1):
            while stack and height[stack[-1]] < height[curr]:
                stack.pop()
            if stack:
                res[curr] = min(res[curr], height[stack[0]])
            stack.append(curr)
        for curr in stack:
            res[curr] = 0

        for i in range(len(res)):
            if res[i]:
                res[i] -= height[i]
        return sum(res)

    def _dp_trap(self, height: List[int]) -> int:
        n = len(height)

        dp_left_height = [0] * n
        dp_left_height[0] = height[0]
        for i in range(1, n):
            dp_left_height[i] = max(dp_left_height[i - 1], height[i])
        dp_right_height = [0] * n
        dp_right_height[-1] = height[-1]
        for i in range(n - 2, -1, -1):
            dp_right_height[i] = max(dp_right_height[i + 1], height[i])

        res = 0
        for i in range(n):
            res += min(dp_left_height[i], dp_right_height[i]) - height[i]

        return res

    def _dp_old_trap(self, height: List[int]) -> int:
        left = [0] * len(height)
        right = [0] * len(height)
        left[0] = height[0]
        right[-1] = height[-1]
        for idx in range(1, len(height)):
            left[idx] = max(left[idx - 1], height[idx])

        for idx in range(len(height) - 2, -1, -1):
            right[idx] = max(right[idx + 1], height[idx])

        res = 0
        for idx in range(1, len(height) - 1):
            res += (max(0, min(left[idx], right[idx]) - height[idx]))
        return res

    def trap(self, height: List[int]) -> int:
        left_idx = 0
        left_max = height[left_idx]
        right_idx = len(height) - 1
        right_max = height[right_idx]

        res = 0
        while left_idx < right_idx:
            if left_max > right_max:
                right_idx -= 1
                if height[right_idx] > right_max:
                    right_max = height[right_idx]
                else:
                    res += right_max - height[right_idx]
            else:
                left_idx += 1
                if height[left_idx] > left_max:
                    left_max = height[left_idx]
                else:
                    res += left_max - height[left_idx]

        return res


assert_value(6, Solution().trap, height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
assert_value(9, Solution().trap, height=[4, 2, 0, 3, 2, 5])
